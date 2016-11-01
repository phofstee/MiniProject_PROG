__author__ = "Thomas Korevaar, Menno Noltes, Gijs van Ewijk, Larsse Vink and Pim Hofstee"
__version__ = 1.0
__status__ = 'Development'

from register import register
from park import park

def menu():

    print('Menu: ')
    print('1 - Fiets stallen')
    print('3 - Fiets ophalen')
    print('4 - Status fiets opvragen')
    print('')

    try:
        input_choice = int(input('Maak een keuze: '))
        if input_choice > 0 and input_choice < 5:
            if input_choice == 1:
                # todo: extra beveiliging > registratie?
                park()
            if input_choice == 2:
                # @todo: wachtwoord encrypten bij opslaan?
                register()
            if input_choice == 3:
                print('Fiets ophalen')
            if input_choice == 4:
                print('Status fiets opvragen')
        else:
            print('Geen geldige invoer!')
    except:
        print('')
        print('Ongeldige waarde!')

    # Na dat de functie is uitgevoerd, moet het menu opnieuw worden gestart.
    menu()