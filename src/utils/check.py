from os import getenv
from os.path import (expanduser, join)
from requests import get

class Check:

    def connection(self):
        try:
            return get(getenv('URL_GOOGLE'))
        except Exception:
            return False

    def default_dir(self):
        return getenv('DEFAULT_DIR') % expanduser('~')

    def assets_dir(self):
        return join(self.default_dir(),'assets')


    