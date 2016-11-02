__author__ = "Pim en Thomas"

import sqlconnection
import twostep

def AttemptRegister(username, password):

    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    stallingData = sqlconnection.GetAllRows(sqlcursor)

    # Maak een list van alle gebruikers
    users = []
    errormessage = None

    usernameCleared = True
    passwordCleared = True

    for row in stallingData:
        users.append(row[1])

    # Maak een username
    try:
        if username in users:
            errormessage = 'Deze gebruikersnaam is al in gebruik\nkies a.u.b. een nieuwe.'
            usernameCleared = False
        if len(username) == 0:
            errormessage = 'U heeft geen gebruikersnaam ingevoerd\nProbeer het nogmaals.'
            usernameCleared = False
        if len(username) > 24:
            errormessage = 'De gebruikersnaam mag maximaal\n24 karakters lang zijn\nProbeer het nogmaals.'
            usernameCleared = False
    except:
        errormessage = 'Ongeldige gebruikersnaam opgegeven\nprobeer nogmaals.'
        usernameCleared = False

    # Maak een wachtwoord
    if len(password) <= 0:
        errormessage = 'Ongeldig wachtwoord opgegeven\nprobeer het nogmaals.'
        passwordCleared = False

    # Als username en wachtwoord zijn aangemaakt, data opslaan
    if usernameCleared and passwordCleared:

        dataobject = { "username" : username, "password" : password, "secret" : twostep.GetSecret(), "storagestate" : "0", "storagedate" : "" }
        sqlconnection.CreateNewRow(sqlconn, sqlcursor, dataobject)

        return True, 'Het account\n{}\nis succesvol aangemaakt'.format(username)
    else:
        return False, errormessage