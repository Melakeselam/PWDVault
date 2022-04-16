from numpy import equal
from ui.Menus import Menus
from ui.main_menu_sub_menus.PlatformMenu import PlatformMenu
from service.PlatformService import PlatformService
from service.dtos.PlatformDto import PlatformDto
from service.CategoryService import CategoryService
from service.dtos.CategoryDto import CategoryDto, PasswordRetentionPeriod
from utils.UiUtils import UiUtils
import sys
import os
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
sys.path.append(os.path.abspath(os.path.join('..', 'persistence')))


class CategoryMenu:
    category_service = CategoryService()
    
    def __init__(self, user_id) -> None:
        self.user_id = user_id
        self.platform_menu = PlatformMenu(user_id)

    def exec_category_menu(self):
        category_menu_level = True
        while category_menu_level:
            UiUtils.clear()
            menu_choice = UiUtils.disp_and_select_from_menu(Menus.category_menu)
            category_menu_level = self.exec_category_menu_choice(int(menu_choice))
        return category_menu_level

    def exec_category_menu_choice(self, choice):
        if choice == 1:
            self.add_category_menu(),
        elif choice == 2:
            self.remove_category_menu(),
        elif choice == 3:
            self.update_category_menu(),
        elif choice == 4:
            self.show_categories_menu_onPause(True),
        elif choice == 5:
            return False
        else:
            input("This menu choice is not available!")
        return True

    def add_category_menu(self):
        try:
            UiUtils.clear()
            self.platform_menu.show_platforms_menu_on_pause(False)
            self.show_categories_menu_onPause(False)
            print("\n")
            print("ADD CATEGORY")
            print("------------")
            platform_id = int(input("Platform Id: "))
            name = input("Name: ")
            description = input("Description: ")
            password_retention_period = input("Password Retention Period (years-months-days-hours): ")
            categoryDto = None
            if password_retention_period is not None:
                period = password_retention_period.split('-')
                period = [int(x) for x in period]
                input(period)
                if len(period) == 4: 
                    categoryDto = CategoryDto(platform_id,
                        name,
                        description,
                        PasswordRetentionPeriod(*period))
            else:
                categoryDto = CategoryDto(platform_id,
                        name,
                        description)
            self.category_service.add_category(categoryDto)
            return True
        except Exception as e:
            input("ERR: Add Category failed!", e)
            return False

    def remove_category_menu(self):
        try:
            UiUtils.clear()
            self.show_categories_menu_onPause(False)
            print("REMOVE CATEGORY")
            print("---------------")
            id = int(input("Platform id: "))
            name = input("Category name: ")
            self.category_service.remove_category(id, name)
            return True
        except Exception as e:
            input("ERR: Remove Category failed!",e)
            return False

    def update_category_menu(self):
        try:
            UiUtils.clear()
            category_dtos = self.show_categories_menu_onPause(False)
            print("UPDATE CATEGORY")
            print("---------------")
            platform_id = int(input("Platform Id: "))
            name = input("Category Name: ")
            update_category = None
            
            for category in category_dtos:
                if category.platform_id() == platform_id and category.name() == name:
                    update_category = category
                    break
            if update_category is None:
                input(f'no record with platform id: {platform_id} and category name: {name} was found to update.')
                return False

            description = input(f"Category Description: ['{update_category.description()}'] ")
            if (description is not None) and (description != "") and (update_category.description() != description):
                update_category.description(description)

            password_retention_period = input(f"Password Retention Period (years-months-days-hours): [{str(update_category.password_retention_period())}]")
            if (password_retention_period is not None) and (password_retention_period != ""):
                period_values_arr = password_retention_period.split('-')
                period_values_arr = [int(x) for x in period_values_arr]
                input(period_values_arr)
                if len(period_values_arr) == 4 and update_category.password_retention_period().values() != period_values_arr: 
                    update_category.password_retention_period(
                        PasswordRetentionPeriod(*period_values_arr))

            input(f'setupMenu:: update_category: {str(update_category)}')
            self.category_service.update_category(update_category)
            return True
        except Exception as e:
            input("ERR: Update Category failed!",e)
            return False

    def show_categories_menu_onPause(self, pause):
        try:
            if pause:
                UiUtils.clear()
            field_names = ["PLATFORM_ID", "NAME",
                           "DESCRIPTION", "PWD_RETENTION"]
            category_dtos = self.category_service.get_all()

            print("\t\tCATEGORIES TABLE")
            print("\t\t================")
            UiUtils.dispTable(field_names, category_dtos)
            if pause:
                input("Press <enter> to return to menu...")
            return category_dtos
        except Exception as e:
            input(f"ERR: exception occured in Table 'Categories' : {str(e)}")
            return False

    def show_category_id_name_columns_on_pause(self, pause):
        try:
            UiUtils.clear()
            field_names = ["PLATFORM_ID", "CATEGORY_NAME"]
            category_maps = [dict(platform_id=categroy.platform_id(), category_name=categroy.name())
                            for categroy in self.category_service.get_all()]
            UiUtils.disp_as_columns(field_names, category_maps)
            if pause:
                input("Press <enter> to continue...")
        except Exception as e:
            input(
                f"ERR: exception occured while displaying 'Categories' as columns: {str(e)}")
            return False
