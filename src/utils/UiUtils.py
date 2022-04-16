from dis import dis
from lib2to3.pgen2.token import NAME
from os import system, name
import numpy as np
import pyautogui

char_size_in_px = 8

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

    def disp_table(titles, entities):
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
        for entity in entities:
            values = entity.values()
            print(rowTemplate.format(*values))
        print("=" * (len(titleRow) + tabs*5))

    def disp_and_select_from_menu(menu):
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

    
    def request_input(inputRequests):
        display = f"\n     PWDVault CREDENTIALS MANAGEMENT SYSTEM\n \
    -----------------------------------------------\n\n\
    {inputRequests['title']}\n --------------------------------\n"
        responses = {}
        keys = [*inputRequests.keys()]
        print(display)
        for i in range(1, len(inputRequests), 1):
            responses[keys[i]] = input(inputRequests[keys[i]])
        return responses

    def prep_row_disp(elements, disp_width):
        disp = ' : '.join(elements)
        padding = (disp_width - len(disp)) // 2
        if padding > 0:
            sp = ' '
            disp = f'{sp*padding}{disp}{sp*padding}'
        return disp

    def disp_as_columns(fields, entity_map_list):
        
        scr_width_px, scr_height_px = pyautogui.size()
        scr_width = scr_width_px // char_size_in_px
        min_col_key_width = sum([len(field) for field in fields])
        max_field_value_widths = [0 for i in range(len(fields))]
        for entity_map in entity_map_list:
            for i in range(len(fields)):
                max_field_value_widths[i] = max(max_field_value_widths[i],len(str(entity_map[fields[i].lower()])))

        min_col_values_width = sum(max_field_value_widths)
        min_col_width = max(min_col_key_width, min_col_values_width) + len(fields) * 3
        nbr_cols = scr_width // min_col_width
        col_width = min_col_width

        col_titles_for_disp = UiUtils.prep_row_disp(fields, col_width)
        cols_of_entities_for_disp = [[] for i in range(nbr_cols)]
        max_nbr_entities_per_col = len(entity_map_list) // nbr_cols + 1

        for i in range(len(entity_map_list)):
            cols_of_entities_for_disp[i // max_nbr_entities_per_col] \
                .append(UiUtils.prep_row_disp(map(str,entity_map_list[i].values()), col_width))

        title_row = '|'.join([col_titles_for_disp for i in range(len(entity_map_list))])
        print(title_row)
        print('='*len(title_row))
        for i in range(max_nbr_entities_per_col):
            row = []
            for col in cols_of_entities_for_disp:
                if i < len(col):
                    row.append(col[i])
            print('|'.join(row))
        print()
