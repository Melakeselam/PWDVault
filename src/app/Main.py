import sys
import os
from config.configuration import Configuration
from ui.LoginMenu import LoginMenu
# sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
from utils.UiUtils import UiUtils
from ui.MainMenu import MainMenu


class Main:

    def __init__(self) -> None:
        self.app_config = Configuration('application')

    def orchestrator(self):
        try:
            user_id = 1 if self.app_config.get('environment') =='dev' \
                else LoginMenu().exec_login_menu()
            if user_id > 0:
                MainMenu(user_id).exec_main_menu()
            print('Program was exited. Good bye!')
        except:
            sys.exit('Exception was encountered. Program was stopped, deal with it!')
