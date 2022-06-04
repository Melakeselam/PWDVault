import re
from src.service.HostService import HostService
from src.app.Main import AppContext
from src.ui.main_menu_sub_menus.HostCommandMenu import HostCommandMenu
from src.ui.main_menu_sub_menus.HostQueryMenu import HostQueryMenu
from src.ui.main_menu_sub_menus.PlatformMenu import PlatformMenu
from src.utils.UiUtils import UiUtils
from src.ui.main_menu_sub_menus.CategoryMenu import CategoryMenu
import sys
import os
from src.ui.Menus import Menus
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))


class MainMenu:
    def __init__(self, app:AppContext, user_id) -> None:
        self._user_id = user_id
        self._category_menu = CategoryMenu(app, self._user_id)
        self._platform_menu = PlatformMenu(app, self._user_id)
        self._host_query_menu = HostQueryMenu(app, self._user_id)
        self._host_command_menu = HostCommandMenu(app, self._user_id)
        self._host_service = HostService(app, self._user_id)
        # self._grouped_critical_hosts = self._host_service.retrieve_critical_pwd_grouped_by_severity(self._user_id)

    def exec_main_menu(self):
        main_menu_level = True
        while main_menu_level:
            UiUtils.clear()
            # UiUtils.disp_critical_pwd_summary_banner(self._grouped_critical_hosts)
            menu_choice = UiUtils.disp_and_select_from_menu(Menus.main_menu)
            main_menu_level = self.exec_main_menu_choice(int(menu_choice))

    def exec_main_menu_choice(self, choice):
        if choice == 1:
            self._host_query_menu.exec_query_credentials_menu()
        elif choice == 2:
            print()
            # self._host_command_menu.exec_update_for_critical_passwords(self._grouped_critical_hosts)
        elif choice == 3:
            input("Add New Host")
        elif choice == 4:
            input("Manage Hosts")
        elif choice == 5:
            self._platform_menu.exec_platform_menu()
        elif choice == 6:
            self._category_menu.exec_category_menu()
        elif choice == 7:
            return False
        else:
            input("This menu choice is not available!")
        return True
