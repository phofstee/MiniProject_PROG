# @TODO: IMPORTS
import _sqlite3
import os

# Functie om het scherm op te schonen.
# @AUTHOR: Pim
def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Functie om het menu te starten
# @AUTHOR: Pim
import menu

# Iedere module hier importeren
# @AUTHOR: iedereen

# @TODO: DB CONNECTIE
import sqlconnection

# @TODO: REGISTREER
import register

# @TODO: STALLEN
# @AUTHOR:

# @TODO: OPHALEN
# @NOTE: Hier krijg je
# @AUTHOR:

# @TODO: INFO OPVRAGEN
# @AUTHOR:

menu.menu()
