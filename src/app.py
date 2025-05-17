from dotenv import load_dotenv
from FreeSimpleGUI import (theme, WIN_CLOSED)
from utils.check import Check
from utils.layout import Layout
from utils.notify import Notify
from utils.set import Set


class App:

    load_dotenv()
    theme('DarkGrey11')
    def __init__(self):
        self.__set = Set(Check())
        self.__layout = Layout(self.__set.logo(), self.__set.icon())
        self.__notify = Notify(self.__set, self.__layout)

    def chooseDir(self):
        self.chooseDirWindow = self.__layout.chooseDir(
            self.__set.screen((0.5859375, 0.4166666666666667))
        )

        while True:
            event, values = self.chooseDirWindow.read()
            if event == WIN_CLOSED:
                break
            if event == 'Salvar':
                if values['dir']:
                    self.chooseDirWindow.Hide()
                    return values['dir']

    def main(self) -> None:
        try:
            if not Check().connection():
                self.__notify.net()
            else:
                if self.__set.dir():
                    self.mainWindow = self.__layout.main(
                        self.__set.screen(
                            (0.5859375, 0.4166666666666667)
                        )
                    )
                    while True:
                        event, values = self.mainWindow.read()
                        if event == WIN_CLOSED:
                            break
                        if event == 'Enviar':
                            if '--/--/--' not in values.values():
                                self.mainWindow.Hide()
                                if self.__notify.stats(values):
                                    self.__dir = self.chooseDir()
                                    if self.__dir:
                                        self.__notify.reportium(
                                            values, self.__dir
                                        )
                        self.mainWindow.UnHide()
        except Exception as error:
            print(error)

if __name__ == '__main__':
    App().main()
        