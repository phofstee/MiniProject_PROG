__author__ = "Pim Hofstee"

import sqlconnection
import time

def register():

    # settings for SQL connection
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    stallingData = sqlconnection.GetAllRows(sqlcursor)

    # create a list of all users
    users = []

    for row in stallingData:
        users.append(row[1])

    print('We gaan uw fiets nu registeren.\n')

    # create username
    name = str.lower(input('Geef uw gebruikersnaam op: '))
    while name in users or len(name) <= 0:
        try:
            if name in users:
                print('')
                print('Deze gebruikersnaam is al in gebruik, kies a.u.b. een nieuwe.')
                name = str.lower(input('Geef uw gebruikersnaam op: '))
            if len(name) == 0:
                print('')
                print('U heeft geen gebruikersnaam ingevoerd. Probeer het nogmaals.')
                name = str.lower(input('Geef uw gebruikersnaam op: '))

        except:
            print('Ongeldige gebruikersnaam opgegeven, probeer nogmaals.')

    #create password
    password = str(input('Geef uw wachtwoord op: '))
    while len(password) <= 0:
        try:
            password = str(input('Geef uw wachtwoord op: '))
        except:
            print('Ongeldig wachtwoord opgegeven, probeer nogmaals.')

    # Fill object and store
    dataobject = { "username" : name, "password" : password, "storagestate" : "0", "storagedate" : "" }
    sqlconnection.CreateNewRow(sqlconn, sqlcursor, dataobject)

    print('Het account', name, 'is succesvol aangemaakt')
    print('')
    time.sleep(2)

def AttemptRegister(username, password):
    # settings for SQL connection
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    stallingData = sqlconnection.GetAllRows(sqlcursor)

    # create a list of all users
    users = []
    errormessage = None

    usernameCleared = True
    passwordCleared = True

    for row in stallingData:
        users.append(row[1])

    # create username
    try:
        if username in users:
            errormessage = 'Deze gebruikersnaam is al in gebruik\nkies a.u.b. een nieuwe.'
            usernameCleared = False
        if len(username) == 0:
            errormessage = 'U heeft geen gebruikersnaam ingevoerd\nProbeer het nogmaals.'
            usernameCleared = False
    except:
        errormessage = 'Ongeldige gebruikersnaam opgegeven\nprobeer nogmaals.'
        usernameCleared = False

    #create password
    if len(password) <= 0:
        errormessage = 'Ongeldig wachtwoord opgegeven\nprobeer het nogmaals.'
        passwordCleared = False

    if usernameCleared and passwordCleared:
        # Fill object and store
        dataobject = { "username" : username, "password" : password, "storagestate" : "0", "storagedate" : "" }
        sqlconnection.CreateNewRow(sqlconn, sqlcursor, dataobject)

        return True, 'Het account {} is succesvol aangemaakt'.format(username)
    else:
        return False, errormessage