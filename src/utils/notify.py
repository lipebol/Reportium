from textwrap import TextWrapper

class Notify:

    def __init__(self, Set: object, Layout: object) -> None:
        self.__set, self.__layout = Set, Layout
        
    def net(self):
        self.netWindow = self.__layout.generic(
            self.__set.screen((0.21961932650073207, 0.13020833333333334)),
            '[:/] sem Internet.'
        )

        while True:
            event, values = self.netWindow.read()
            if event == 'Exit':
                self.netWindow.Hide()
                break

    def stats(self, dates: dict):
        self.__data = self.__set.data(dates)
        self.statsWindow = self.__layout.stats(
            self.__set.screen(
                (0.4685212298682284, 0.2864583333333333)
            ), dates, self.__data
        ) if type(self.__data) == list else self.__layout.generic(
            self.__set.screen((0.43191800878477304, 0.13020833333333334)),
            TextWrapper(width=40).fill(text=f"{''.join(self.__data.values())}") 
        )

        while True:
            event, values = self.statsWindow.read()
            if event == 'Exit':
                self.statsWindow.Hide()
                break
            if event == 'Continuar':
                self.statsWindow.Hide()
                return True

    def reportium(self, dates: dict, dir: str):
        self.reportiumWindow = self.__layout.generic(
            self.__set.screen(
                (0.21961932650073207, 0.13020833333333334)
            ), 'Concluído com Sucesso!'
        )

        while not self.__set.data(dates, dir):
            event, values = self.reportiumWindow.read()
            if event == 'Exit':
                self.reportiumWindow.Hide()
                break        
        self.reportiumWindow.Hide()
        return True