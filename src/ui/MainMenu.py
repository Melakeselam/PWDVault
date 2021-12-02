import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
from ui.main_menu_sub_menus.SetupMenu import SetupMenu
from utils.UiUtils import UiUtils


class MainMenu:
    def __init__(self) -> None:
        pass

    def execMainMenuChoice(self, choice):
        if choice == 1:
            print("Create Credentials")
        elif choice == 2:
            print("Retrieve Credentials")
        elif choice == 3:
            print("Update Expired Passwords")
        elif choice == 4:
            print("Show all Expired Passwords")
        elif choice == 5:
            print("Show Categories")
        elif choice == 6:
            SetupMenu().execSetupMenu()
        elif choice == 7:
            return False
        else:
            print("This menu choice is not available!")
        return True
