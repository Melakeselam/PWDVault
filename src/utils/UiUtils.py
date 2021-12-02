from os import system, name
import numpy as np


class UiUtils:

    def __init__(self) -> None:
        pass

    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

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
