import time
import main

def menu():

    print('Menu: ')
    print('1 - Registreer')
    print('2 - Bla')
    print('3 - Bla')
    print('')

    try:
        input_choice = int(input('Maak een keuze: '))

        if input_choice > 0 and input_choice < 4:
            if input_choice == 1:
                print('')
                print('U fiets wordt geregistreerd')
                time.sleep(2)
                main.clearscreen()
            if input_choice == 2:
                print('')
                print('Bla')
                time.sleep(2)
                main.clearscreen()
            if input_choice == 3:
                print('')
                print('Bla')
                time.sleep(2)
                main.clearscreen()
        else:
            print('')
            print('Geen geldige invoer!')
            time.sleep(1)
            main.clearscreen()


    except:
        print('')
        print('Ongeldige waarde!')
        time.sleep(1)
        main.clearscreen()
