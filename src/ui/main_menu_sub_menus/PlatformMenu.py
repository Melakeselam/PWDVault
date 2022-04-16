from numpy import equal
from ui.Menus import Menus
from service.PlatformService import PlatformService
from service.dtos.PlatformDto import PlatformDto
from service.CategoryService import CategoryService
from service.dtos.CategoryDto import CategoryDto, PasswordRetentionPeriod
from utils.UiUtils import UiUtils
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
sys.path.append(os.path.abspath(os.path.join('..', 'persistence')))


class PlatformMenu:
    platform_service = PlatformService()

    def __init__(self, user_id) -> None:
        self.user_id = user_id

    def exec_platform_menu(self):
        platform_menu_level = True
        while platform_menu_level:
            UiUtils.clear()
            menu_choice = UiUtils.disp_and_select_from_menu(
                Menus.platform_menu)
            platform_menu_level = self.exec_platform_menu_choice(
                int(menu_choice))
        return platform_menu_level

    def exec_platform_menu_choice(self, choice):
        if choice == 1:
            self.add_platform_menu()
        elif choice == 2:
            self.remove_platform_menu()
        elif choice == 3:
            self.update_platform_menu()
        elif choice == 4:
            self.show_platforms_menu_on_pause(True),
        elif choice == 5:
            return False
        else:
            input("This menu choice is not available!")
        return True

    def add_platform_menu(self):
        try:
            UiUtils.clear()
            self.show_platforms_menu_on_pause(False)
            print("\n")
            print("ADD PLATFORM")
            print("------------")
            name = input("Platform Name: ")
            description = input("Description: ")

            self.platform_service.add_platform(
                PlatformDto(None, name, description))
            return True
        except Exception as e:
            input("ERR: Add Platform failed!", e)
            return False

    def remove_platform_menu(self):
        try:
            UiUtils.clear()
            self.show_platforms_menu_on_pause(False)
            print("REMOVE PLATFORM")
            print("---------------")
            id = input("Platform id: ")
            self.platform_service.remove_platform(id)
            return True
        except Exception as e:
            input("ERR: Remove Platform failed!", e)
            return False

    def update_platform_menu(self):
        try:
            UiUtils.clear()
            platform_dtos = self.show_platforms_menu_on_pause(False)
            print("UPDATE PLATFORM")
            print("---------------")
            id = input("Platform Id: ")
            update_platform = None
            for platform in platform_dtos:
                if platform.id() == int(id):
                    update_platform = platform
                    break

            name = input(f"Platform Name ({update_platform.name()}): ")
            description = input(
                f"Platform Description ({update_platform.description()}): ")
            if (name is not None) and (update_platform.name() != name):
                update_platform.name(name)
            if (description is not None) and (update_platform.description() != description):
                update_platform.description(description)
            input(f'setupMenu: {str(update_platform)}')
            self.platform_service.update_platform(update_platform)
            return True
        except Exception as e:
            input("ERR: Remove Platform failed!", e)
            return False

    def show_platforms_menu_on_pause(self, pause):
        try:
            if pause:
                UiUtils.clear()
            field_names = ["ID", "NAME", "DESCRIPTION"]
            platform_dtos = self.platform_service.get_all()

            print("\t\tPLATFORMS TABLE")
            print("\t\t===============")

            UiUtils.disp_table(field_names, platform_dtos)
            if pause:
                input("Press <enter> to return to menu...")
            return platform_dtos
        except Exception as e:
            input(f"ERR: exception occured in Table 'Platform' : {str(e)}")
            return False

    def show_platforms_id_name_columns_on_pause(self, pause):
        try:
            UiUtils.clear()
            field_names = ["ID", "NAME"]
            platform_maps = [dict(id=platform.id(), name=platform.name())
                            for platform in self.platform_service.get_all()]
            UiUtils.disp_as_columns(field_names, platform_maps)
            if pause:
                input("Press <enter> to continue...")
        except Exception as e:
            input(
                f"ERR: exception occured while displaying 'Platforms' as columns: {str(e)}")
            return False
