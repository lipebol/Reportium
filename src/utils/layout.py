from os import getenv
from FreeSimpleGUI import (
    Button, CalendarButton, Column, FolderBrowse, 
    Image, Input, Text, theme_background_color, Window
)


class Layout:
    
    def __init__(self, logo, icon) -> None:
        self.logo, self.icon = logo, icon

    def main(self, screen: object) -> object:
        self.size_x, self.loc_x, self.size_y, self.loc_y = tuple(screen)
        return Window(
            getenv('NAME'), icon=self.icon, layout=[ 
                [Text('')],
                [Column([[Image(filename=self.logo)]])],
                [
                    Column([self.title('  Data Inicial  ')]),
                    Column([self.title('  Data Final  ')])
                ],
                [
                    Text(' '),
                    Column([self.calendar('start_date')]), 
                    Text('      '),
                    Column([self.calendar('end_date')])
                ],
                [Text('')],
                [Button('Enviar', font=getenv('DEFAULT_FONT'), bind_return_key=True)]
            ],
            size=(self.size_x, self.size_y), grab_anywhere=True, alpha_channel=.9, 
            element_justification='c', location=(self.loc_x, self.loc_y)
        )

    def generic(self, screen: object, message: str) -> object:
        self.size_x, self.loc_x, self.size_y, self.loc_y = tuple(screen)
        return Window(
            getenv('NAME'), layout=[
                [Column([[self.button()]], justification='right')],
                [
                    Column(
                        [[Text(message, font=getenv('DEFAULT_FONT'))]], 
                        justification=getenv('DEFAULT_JUSTIFICATION')
                    )
                ],
                [Text('')],
            ],
            size=(self.size_x, self.size_y), resizable=True, grab_anywhere=True, 
            alpha_channel=.9, no_titlebar=True, location=(self.loc_x, self.loc_y)
        )

    
    def stats(self, screen: object, dates: dict, response: list or dict) -> object:
        self.size_x, self.loc_x, self.size_y, self.loc_y = tuple(screen)
        return Window(
            getenv('NAME'), layout=[
                [Column([[self.button()]], justification='right')],
                [Text('')],
                [
                    Column(
                        [[
                            Text(
                                f"Para o período de {dates['start_date']} a {dates['end_date']},\n   foram localizados {response[0].get('total_registros')} registros.",
                                font=getenv('DEFAULT_FONT')
                            )
                        ]], justification=getenv('DEFAULT_JUSTIFICATION')
                    )
                ],
                [Text('')],
                [
                    Column(
                        [[Button('Continuar', font=getenv('DEFAULT_FONT'), bind_return_key=True)]], 
                        justification=getenv('DEFAULT_JUSTIFICATION')
                    )
                ],
                [Text('')],
            ],
            size=(self.size_x, self.size_y), resizable=False, grab_anywhere=False, 
            no_titlebar=True, location=(self.loc_x, self.loc_y)
        )

    def chooseDir(self, screen: object):
        self.size_x, self.loc_x, self.size_y, self.loc_y = tuple(screen)
        return Window(
            getenv('NAME'), icon=self.icon, layout=[
                [Text('')],
                [Column([[Image(filename=self.logo)]])],
                [Column([self.title('Selecione a pasta para salvar o arquivo:')])],
                [Column([[Input(key='dir'), FolderBrowse('➤', font=getenv('DEFAULT_FONT'))]])],
                [Text('')],
                [Button('Salvar', font=getenv('DEFAULT_FONT'), bind_return_key=True)]
            ],
            size=(self.size_x, self.size_y), grab_anywhere=True, alpha_channel=.9, 
            element_justification='c', location=(self.loc_x, self.loc_y)
        )

    def title(self, title: str) -> object:
        return [Text(title, font=(getenv('DEFAULT_FONT'), 13))]

    def calendar(self, id: str) -> object:
        return [ 
            CalendarButton(
                '➤',no_titlebar=True, locale='pt_BR', begin_at_sunday_plus=1,
                close_when_date_chosen=True, target=id, format='%d/%m/%Y',  
                month_names=(
                    'Janeiro','Fevereiro','Março','Abril','Maio','Junho', 
                    'Julho','Agosto','Setembro','Outubro','Novembro','Dezembro'
                ), day_abbreviations=('Dom','Seg','Ter','Qua','Qui','Sex','Sab')
            ), Input('--/--/--', key=id, size=(10,1), font=(getenv('DEFAULT_FONT'), 11))
        ]

    def button(self):
        return Button(
            '', image_data=self.closeBase64(), border_width=0, 
            key='Exit', button_color=(theme_background_color())
        )

    def closeBase64(self):
        return b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIf\
        AhkiAAAAAlwSFlzAAAAsQAAALEBxi1JjQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXB\
        lLm9yZ5vuPBoAAANJSURBVEiJtZXfa1tlGMc/z0lYVqXghTA3KP2xZlvdSjo7+yMNySpn2\
        hVBL0R2Mbx1Yv8dNxDEOztvh8wyZVsz2zWJztaatDVpShesVtiF9GJJ6XkfL056evJLg7A\
        XDueF9znfz/N9n/c8L7zgIe0EreSeXjCWRFT1BAYUsxtAlofOd2f/N2CxVOroeB6cQfVj1\
        JxGFQVQRVUBBdVNFb2195J8NtnbW24bsFrYjTqqt1HtcoUV1H2aQFB0Wxy5NhzpXarXshr\
        Ei399aJD7gnQhAiII7tud475F3Pzc9W4N6INMtvjBvzpYLTyLquh90JB6Gfuz/08nZXFk0\
        u/Ec7BYKnVgyW1EQuBmuP7bZl32jU6yuQ2/k+Ma0Nl8Ph9qAHQ6nTOIdB2KrG8U+Wr2G76\
        dm28JuXPnHl98+TW/ZmsgPX/vB2YaAILc8IucO9dPIj7K49Qyd5tA7s49JLmQ4XIiyuDgQ\
        G1N1LpRA8g93buASF+9iG3HSMRHWaqDzN1LMp9MkYiP8f577zQpPP1PstuvAwQBVCTiOVF\
        QOZrbdoyDA4eFxR8RQNXw6Ic08fgo7159i2q5EVW0Whu37iYC5IIAKCfFBTWFTE0lCAYDz\
        CdTGOMQm3iT6elJUK2LPYIY5JTnwLJQo+IFNIOIWFiWWzKxAghSs14PscRSD4AG/hAxqC/\
        A/+F33y+w+PgJ0fFLqBpvu65OJVpDlB0PYILWijiKCA2Q+Qcp0plfGB97g7ftCRT1tkuB6\
        RYQDTgrHuD8yVA29/vzPErYD3mYzLCUXmF05CK2Pe7tuW3HXHgyBc0hheEzPWveMQUQ5HO\
        qx0xEKBRLpDOrjIwMceXKRMN/YNsxJqKXWEots7ZRrF+/eaRbHVtberx8rLKuaHf1nFEob\
        HO6r8vrO81608b6JmfP9uLrXVsvszcQDocrNQCAtZ39YdQ8UrTjEKJ1za1lA3RjyxhzOXL\
        mtdShZk27Hjh17Cex5CNByv7t8je3xqZXnSNlRK/7xRscHI7cn/tj4phZRXvadLLlYK4N9\
        b2artdqeWXm8xo66Kh8qqKfoNrfFGI0D+ZW6OCVm+GwVJrptHXpr+5UBoKOuaiiJwwGUXa\
        Noz8P9nSutfP9Cx3/AEm78nl/zEWGAAAAAElFTkSuQmCC'