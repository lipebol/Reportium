from ast import literal_eval
from datetime import datetime
from inspect import currentframe
from os import (getenv, makedirs)
from os.path import (abspath, isdir)
from platform import system
import pyarrow as arrow
import pyarrow.compute as arrowcompute
import pyarrow.csv as arrowcsv
from requests import get
from subprocess import (run, PIPE)


class Set:

    def __init__(self, Check: object) -> None:
        self.__check, self.system = Check, system()

    def __request(self, args: str, page=''):
        try:
            return get(
                getenv('ENDPOINT_MAIN') % (
                    getenv('SEPARATOR').join(
                        [str(datetime.strptime(date,'%d/%m/%Y').date()
                        ) for date in args.values() if date != '']
                    ), page
                )
            ).json()
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
            
    def logo(self) -> str:
        return abspath(getenv('LOGO'))
        
    def icon(self) -> str:
        return getenv(f'{self.system}_ICON')

    def screen(self, window_sizes: tuple) -> object:
        for screen_size, window_size in zip(
            [
                int(size.split()[1]) if getenv('NEWLINE') in size 
                else int(size) for size in [
                    run(
                        command, shell=True, stdout=PIPE, text=True
                    ).stdout.strip() for command in getenv(
                        f'{self.system}_SCREEN').split(getenv('SEPARATOR')
                    )
                ]
            ], window_sizes):
                yield int(screen_size * window_size)
                yield (screen_size - int(screen_size * window_size)) // 2

    def dir(self) -> bool:
        try:
            if not isdir(self.__check.default_dir()):
                for dir in [
                    self.__check.default_dir(), self.__check.assets_dir()
                ]:
                    makedirs(dir)
            return True
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
            return False

    def data(self, dates: dict, dir=None) -> list or dict:
        try:
            if not dir:
                return self.__request(dates)
            with arrowcsv.CSVWriter(
                f'{dir}/reportium_{datetime.now().date()}.csv', 
                schema=arrow.schema(self.schema())
            ) as writer:
                for page in range(int(self.__request(dates)[0].get('paginas'))):
                    self.__table = arrow.Table.from_pylist(
                        self.__request(dates, str(page)), 
                        schema=arrow.schema(self.schema())
                    )
                    for idx in range(self.__table.num_columns):
                        match idx:
                            case 1|2|8|9:
                                self.__table = self.__replace(
                                    self.__table, idx, ['T',':00.000Z'], [' ','']
                                )
                            case 10:
                                self.__table = self.__replace(
                                    self.__table, idx, ['.0'], ['']
                                )
                    writer.write(self.__table)
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
        
    def schema(self) -> list:
        try:
            for idx, field in enumerate(literal_eval(getenv('FIELDS'))):
                if idx in (6,):
                    yield arrow.field(field, arrow.int64())
                else:
                    yield arrow.field(field, arrow.string())
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
    
    ### preciso estudar "RegEx" urgente!
    def __replace(self, repltable: object, idx: int, pattern: list, replacement: list) -> object:
        try:
            for n in range(len(pattern)):
                repltable = repltable.set_column(
                    idx, arrow.field(repltable.column_names[idx], arrow.string()),
                    arrowcompute.replace_substring(
                        repltable.column(idx), pattern[n], replacement[n]
                    )
                )
            return repltable
        except Exception as error:
            print(f"{error} in: @{currentframe().f_code.co_name}")
        


