
# import os
# import sys
# sys.path.append(os.path.abspath(
#     os.path.join('.','persistence', 'persistence')))
# sys.path.append(os.path.abspath(os.path.join('.','app', 'Main')))
from persistence.persistence import Persistence
from app.Main import Main


# from ui import orchestrator

# define clear function


# def startPersistence():
#     setupDb()
#     dropTables()
#     createTables()


Persistence().startPersistence()
Main.orchestrator()
# print(dispAndSelectFromMenu(mainMenu))
# print(dispAndSelectFromMenu(setupMenu))


# arg = {
#     "length": 15,
#     "upper": 1,
#     "num": 1,
#     "special": 1
# }


# generatePassword(arg)
