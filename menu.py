__author__ = "Thomas Korevaar, Menno Noltes, Gijs van Ewijk, Larsse Vink and Pim Hofstee"
__version__ = 1.0
__status__ = 'Development'

from park import park
import main

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
                park()
            if input_choice == 2:
                # Larsse
                print('Fiets ophalen')
            if input_choice == 3:
                # Menno
                print('Status fiets opvragen')
            if input_choice == 4:
                main.loginmenu()
        else:
            print('Geen geldige invoer!')
    except:
        print('')
        print('Ongeldige waarde!')