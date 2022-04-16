from ui.main_menu_sub_menus.HostMenu import HostMenu
from ui.main_menu_sub_menus.PlatformMenu import PlatformMenu
from utils.UiUtils import UiUtils
from ui.main_menu_sub_menus.CategoryMenu import CategoryMenu
import sys
import os
from ui.Menus import Menus
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))


class MainMenu:
    def __init__(self, user_id) -> None:
        self.user_id = user_id
        self.category_menu = CategoryMenu(self.user_id)
        self.host_menu = HostMenu(self.user_id)
        self.platform_menu = PlatformMenu(self.user_id)

    def exec_main_menu(self):
        main_menu_level = True
        while main_menu_level:
            UiUtils.clear()
            menu_choice = UiUtils.disp_and_select_from_menu(Menus.main_menu)
            main_menu_level = self.exec_main_menu_choice(int(menu_choice))

    def exec_main_menu_choice(self, choice):
        if choice == 1:
            self.host_menu.exec_retrieve_credentials_menu()
        elif choice == 2:
            input("Update Credentials")
        elif choice == 3:
            input("Add New Host")
        elif choice == 4:
            input("Manage Hosts")
        elif choice == 5:
            self.platform_menu.exec_platform_menu()
        elif choice == 6:
            self.category_menu.exec_category_menu()
        elif choice == 7:
            return False
        else:
            input("This menu choice is not available!")
        return True
