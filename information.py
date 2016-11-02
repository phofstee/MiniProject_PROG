__author__ = "Menno Noltes"
__version__ = 1.0
__status__ = 'Development'

import sqlconnection

#menu voor persoonlijke data of algemene data
def menu(useruuid):
    print('Menu: ')
    print('1 - Persoonlijke informatie')
    print('2 - Algemene informatie')
    print('')

    try:
        input_choice = int(input('Maak een keuze: '))
        if input_choice > 0 and input_choice < 5:
            if input_choice == 1:
                pers_info(useruuid)
            if input_choice == 2:
                gen_info()
        else:
            print('Geen geldige invoer!')
    except:
        print('')
        print('Ongeldige waarde!')

#persoonlijke data
def pers_info(useruuid):
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    parkingdata = sqlconnection.GetRow(sqlcursor, {"uuid" : useruuid})

    data = {}

    userID = parkingdata[0]
    username = parkingdata[1]
    storagestate = parkingdata[3]
    storagedate = parkingdata[4]

    if storagestate == 1:
        storagestate = 'Ja'
    else:
        storagestate = 'Nee'

    print('Persoonlijke informatie:  ')
    print('Gebruikersnaam: ' + username)
    print('Gebruikers-ID: ' + str(userID))
    print('Fiets in stalling: ' + storagestate)

    if storagedate != '':
        print('Datum en tijd van stalling: ' + storagedate)

    return data

#algemene data
def gen_info():
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    parkingdata = sqlconnection.GetAllRows(sqlcursor)

    userID = []

    for data in parkingdata:
        userID.append(data[0])

    userIDs_amount = len(userID)

    print('Algemene informatie: ')
    print('Er zijn in totaal ' + str(userIDs_amount) + ' gebruikers.')

def ShowChoiceMenu(input, uuid):
    if input == "pers_info":
        #pers_info(uuid)
        sqlconn, sqlcursor = sqlconnection.InitializeSQL()
        return sqlconnection.GetRow(sqlcursor, {"uuid": uuid})
    if input == "gen_info":
        #gen_info()
        sqlconn, sqlcursor = sqlconnection.InitializeSQL()
        return len(sqlconnection.GetAllRows(sqlcursor))