import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'utils')))
from utils.UiUtils import UiUtils
from ui.MainMenu import MainMenu
from ui.Menus import Menus

class Main:
    
    def orchestrator():
        mainMenuLevel = True
        while mainMenuLevel:
            UiUtils.clear()
            menuChoice = UiUtils.dispAndSelectFromMenu(Menus.mainMenu)
            mainMenuLevel = MainMenu().execMainMenuChoice(int(menuChoice))
        exit(0)