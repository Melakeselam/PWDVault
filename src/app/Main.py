import sys
import os
from ui.LoginMenu import LoginMenu
# sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
from utils.UiUtils import UiUtils
from ui.MainMenu import MainMenu


class Main:

    def orchestrator():
        try:
            user_id = LoginMenu().exec_login_menu()
            if user_id > 0:
                MainMenu(user_id).exec_main_menu()
            print('Program was exited. Good bye!')
        except:
            sys.exit('Exception was encountered. Program was stopped, deal with it!')
