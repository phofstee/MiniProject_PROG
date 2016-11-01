__author__ = "Thomas Korevaar, Menno Noltes, Gijs van Ewijk, Larsse Vink and Pim Hofstee"
__version__ = 1.0
__status__ = 'Development'

import time
from park import park

def menu():

    print('Menu: ')
    print('1 - Fiets stallen')
    print('2 - Fiets ophalen')
    print('3 - Status fiets opvragen')
    print('4 - Uitloggen')
    print('')

    try:
        input_choice = int(input('Maak een keuze: '))
        if input_choice > 0 and input_choice < 5:
            if input_choice == 1:
                # Pim
                return {"action" : "park"}
            if input_choice == 2:
                # Larsse
                print('Fiets ophalen')
                return {"action": "retrieve"}
            if input_choice == 3:
                # Menno
                print('Status fiets opvragen')
                return {"action": "info"}
            if input_choice == 4:

                print('Loguit')
                return {"action": "logout"}

                print('U bent uitgelogd')
                time.sleep(2)

        else:
            print('Geen geldige invoer!')
            return {"action": ""}
    except:
        print('')
        print('Ongeldige waarde!')
        return {"action": ""}