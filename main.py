__author__ = "Thomas Korevaar, Menno Noltes, Gijs van Ewijk, Larsse Vink and Pim Hofstee"
__version__ = 1.0
__status__ = 'Development'

# Programma modules
import register
import login
from menu import menu
from park import park

# Geeft menu opties weer
def loginmenu():

    print('Menu: ')
    print('1 - Inloggen')
    print('2 - Registreren')
    print('3 - Uitleg')
    print('')

    input_choice = int(input('Maak een keuze: '))
    if input_choice > 0 and input_choice < 3:
        if input_choice == 1:
            # Pim, Thomas
            success, useruuid = login.login()
            #useruuid bevat de uuid voor volgende queries

            while success:
                action = menu()

                for k,v in action.items():
                    if v == "park":
                        park(useruuid)
                    if v == "info":
                        None
                        #tbi informatie over fiets/stalling
                    if v == "retrieve":
                        None
                        #tbi fiets ophalen
                    if v == "logout":
                        success = False
                        useruuid = None
                        loginmenu()
        if input_choice == 2:
            # Pim
            register.register()
        if input_choice == 3:
            # Menno
            print('Uitleg')
    else:
        print('Geen geldige invoer!')

    loginmenu()

# Roep menu aan bij opstarten script
loginmenu()