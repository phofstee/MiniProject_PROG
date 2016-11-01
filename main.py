__author__ = "Thomas Korevaar, Menno Noltes, Gijs van Ewijk, Larsse Vink and Pim Hofstee"
__version__ = 1.0
__status__ = 'Development'

# Programme modules
from register import register
import login

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
            # Pim
            login.login()
        if input_choice == 2:
            # Pim
            register()
        if input_choice == 3:
            # Menno
            print('Uitleg')
    else:
        print('Geen geldige invoer!')

    loginmenu()

# Roep menu aan bij opstarten script
loginmenu()