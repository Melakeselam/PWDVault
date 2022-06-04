from calendar import c
import sys
from src.app.AppContext import AppContext
from src.ui.LoginMenu import LoginMenu
# sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
from src.utils.UiUtils import UiUtils
from src.ui.MainMenu import MainMenu


class Main:

    def __init__(self) -> None:
        self._app_context = AppContext()

    def app_context(self):
        return self._app_context

    def orchestrator(self):
        try:
            context:AppContext = self.app_context()
            context.persistence().startPersistence()
            user_id = 1 if context.app_config().get('environment') =='dev' \
                else LoginMenu(context).exec_login_menu()
            if user_id > 0:
                MainMenu(context,user_id).exec_main_menu()
            print('Program was exited. Good bye!')
        except:
            sys.exit('Exception was encountered. Program was stopped, deal with it!')
