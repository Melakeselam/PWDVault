from os import system, name
from persistence import insertIntoTable, deleteByField, deleteByFields, findByFieldInTable, findAllInTable, clearTable
from re import T
import numpy as np
from menus import mainMenu, setupMenu


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def addPlatform_menu():
    try:
        clear()
        showPlatforms_menu(False)
        print("\n")
        print("ADD PLATFORM")
        print("------------")
        name = input("Platform Name: ")
        description = input("Description: ")
        id = name.lower()[:3]
        insertIntoTable("Platforms", "id, name, description",
                        (id, name, description))
        return True
    except:
        print("ERR: Add Platform failed!")
        return False


def removePlatform_menu():
    try:
        clear()
        showPlatforms_menu(False)
        print("REMOVE PLATFORM")
        print("---------------")
        name = input("Platform Name: ")
        deleteByField("Platforms", "name", name)
        return True
    except:
        print("ERR: Remove Platform failed!")
        return False


def addCategory_menu():
    try:
        clear()
        showPlatforms_menu(False)
        showCategories_menu(False)
        print("ADD CATEGORY")
        print("------------")
        platform = input("Category Platform: ")
        type = input("Category Type: ")
        description = input("Description: ")
        pwd_retention = input("Password Retention Period(days): ")

        platform_id = platform.lower()[:3]

        found = findByFieldInTable("Platforms", "id", platform_id)
        print(found)
        if len(found) > 0:
            insertIntoTable("Categories", "platform_prefix, type, description,pwd_retention_days ",
                            (platform_id, type, description, pwd_retention))
            return True
        else:
            print("ERR: Platfrom does not exist. Change or Create the Platform before attempting to create a Category")
            return False
    except:
        print("ERR: Add Category failed!")
        return False


def removeCategory_menu():
    try:
        clear()
        showCategories_menu(False)
        print("REMOVE CATEGORY")
        print("---------------")
        prefix = input("Category Platform Prefix: ")
        type = input("Category Platform Prefix: ")
        deleteByFields(
            "Platforms", ["platform_prefix", "type"], [prefix, type])
        return True
    except:
        print("ERR: Remove Platform failed!")
        return False


def dispTable(titles, rows):
    col_count = len(titles)
    rowTemplate = ""
    for col in range(col_count):
        rowTemplate = rowTemplate + "|\t{}\t"
    rowTemplate = rowTemplate + "|"
    titleRow = rowTemplate.format(*titles)
    tabs = col_count * 2
    print("_" * (len(titleRow) + tabs*5))
    print(titleRow)
    print("=" * (len(titleRow) + tabs*5))
    for row in rows:
        rowArr = np.asarray(row)
        print(rowTemplate.format(*rowArr))
    print("=" * (len(titleRow) + tabs*5))


def showPlatforms_menu(pause):
    try:
        if pause:
            clear()
        field_names = ["ID", "NAME", "DESCRIPTION"]
        rows = findAllInTable("Platforms")
        print("\t\tPLATFORMS TABLE")
        print("\t\t===============")

        dispTable(field_names, rows)
        if pause:
            input("Press <enter> to return to menu...")
    except:
        return "ERR: exception occured in Table 'Platform'"


def showCategories_menu(pause):
    try:
        if pause:
            clear()
        field_names = ["PLATFORM_PREFIX", "TYPE",
                       "DESCRIPTION", "PWD_RETENTION_DAYS"]
        rows = findAllInTable("Categories")
        print("\t\tCATEGORIES TABLE")
        print("\t\t================")
        dispTable(field_names, rows)
        if pause:
            input("Press <enter> to return to menu...")
    except:
        return "ERR: exception occured in Table 'Categories'"


def dispAndSelectFromMenu(menu):
    mnuList = ""
    for mnuIndx in range(1, len(menu), 1):
        mnuList = mnuList + "\t{}: {}\n".format(mnuIndx, menu[mnuIndx])
    display = "\
\n     PWDVault CREDENTIALS MANAGEMENT SYSTEM\n \
-----------------------------------------------\n\n \
{}\n \
===========\n \
{} \
--------------------------------\n".format(menu["title"], mnuList)
    print(display)
    return input("Choose Number of Selected Menu Item: ")


def execMainMenuChoice(choice):
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
        execSetupMenu()
    elif choice == 7:
        return False
    else:
        print("This menu choice is not available!")
    return True


def execSetupMenuChoice(choice):
    if choice == 1:
        addPlatform_menu()
    elif choice == 2:
        removePlatform_menu()
    elif choice == 3:
        addCategory_menu(),
    elif choice == 4:
        removeCategory_menu(),
    elif choice == 5:
        showPlatforms_menu(True),
    elif choice == 6:
        showCategories_menu(True),
    elif choice == 7:
        return False
    else:
        print("This menu choice is not available!")
    return True


def execSetupMenu():
    setupMenuLevel = True
    while setupMenuLevel:
        clear()
        menuChoice = dispAndSelectFromMenu(setupMenu)
        setupMenuLevel = execSetupMenuChoice(int(menuChoice))
    return True


def orchestrator():
    mainMenuLevel = True
    while mainMenuLevel:
        clear()
        menuChoice = dispAndSelectFromMenu(mainMenu)
        mainMenuLevel = execMainMenuChoice(int(menuChoice))
    exit(0)
