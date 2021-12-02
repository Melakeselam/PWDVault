from ui.Menus import Menus
from persistence.persistence import Persistence as Persist
from utils.UiUtils import UiUtils
import sys
import os
import uuid
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
sys.path.append(os.path.abspath(os.path.join('..', 'persistence')))


class SetupMenu:
    def __init__(self) -> None:
        pass

    def execSetupMenu(self):
        setupMenuLevel = True
        while setupMenuLevel:
            UiUtils.clear()
            menuChoice = UiUtils.dispAndSelectFromMenu(Menus.setupMenu)
            setupMenuLevel = self.execSetupMenuChoice(int(menuChoice))
        return True

    def execSetupMenuChoice(self, choice):
        if choice == 1:
            self.addPlatform_menu()
        elif choice == 2:
            self.removePlatform_menu()
        elif choice == 3:
            self.addCategory_menu(),
        elif choice == 4:
            self.removeCategory_menu(),
        elif choice == 5:
            self.showPlatforms_menu(True),
        elif choice == 6:
            self.showCategories_menu(True),
        elif choice == 7:
            return False
        else:
            print("This menu choice is not available!")
        return True

    def addPlatform_menu(self):
        try:
            UiUtils.clear()
            self.showPlatforms_menu(False)
            print("\n")
            print("ADD PLATFORM")
            print("------------")
            name = input("Platform Name: ")
            description = input("Description: ")
            # id = str(uuid.uuid4())
            Persist().insertIntoTable("Platforms", "name, description",
                                      (name, description))
            return True
        except:
            print("ERR: Add Platform failed!")
            input()
            return False

    def removePlatform_menu(self):
        try:
            UiUtils.clear()
            self.showPlatforms_menu(False)
            print("REMOVE PLATFORM")
            print("---------------")
            name = input("Platform id: ")
            Persist().deleteByField("Platforms", "id", name)
            return True
        except:
            print("ERR: Remove Platform failed!")
            input()
            return False

    def addCategory_menu(self):
        try:

            UiUtils.clear()
            self.showPlatforms_menu(False)
            self.showCategories_menu(False)
            print("ADD CATEGORY")
            print("------------")
            platform_id = input("Category Platform id: ")
            name = input("Category Name: ")
            description = input("Description: ")
            pwd_retention = input("Password Retention Period(days): ")

            found = Persist().findByFieldInTable("Platforms", "id", platform_id)

            if len(found) > 0:
                Persist().insertIntoTable("Categories", "platform_id, name, description,pwd_retention_days ",
                                          (platform_id, name, description, pwd_retention))
                return True
            else:
                print(
                    "ERR: Platfrom does not exist. Change or Create the Platform before attempting to create a Category")
                input()
                return False
        except:
            print("ERR: Add Category failed!")
            input()
            return False

    def removeCategory_menu(self):
        try:
            UiUtils.clear()
            self.showCategories_menu(False)
            print("REMOVE CATEGORY")
            print("---------------")
            platform_id = input("Category Platform id: ")
            name = input("Category name: ")
            Persist().deleteByFields(
                "Platforms", ["platform_prefix", "type"], [platform_id, name])
            return True
        except:
            print("ERR: Remove Platform failed!")
            input()
            return False

    def showPlatforms_menu(self, pause):

        try:
            if pause:
                UiUtils.clear()
            field_names = ["ID", "NAME", "DESCRIPTION"]
            rows = Persist().findAllInTable("Platforms")
            print("\t\tPLATFORMS TABLE")
            print("\t\t===============")

            UiUtils.dispTable(field_names, rows)
            if pause:
                input("Press <enter> to return to menu...")
        except:
            print("ERR: exception occured in Table 'Platform'")
            input()
            return False

    def showCategories_menu(self, pause):
        try:
            if pause:
                UiUtils.clear()
            field_names = ["PLATFORM_ID", "NAME",
                           "DESCRIPTION", "PWD_RETENTION_DAYS"]
            rows = Persist().findAllInTable("Categories")
            print("\t\tCATEGORIES TABLE")
            print("\t\t================")
            UiUtils.dispTable(field_names, rows)
            if pause:
                input("Press <enter> to return to menu...")
        except:
            print("ERR: exception occured in Table 'Categories'")
            input()
            return False
