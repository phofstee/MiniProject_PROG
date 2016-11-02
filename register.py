__author__ = "Pim Hofstee", "Thomas Korevaar"

import sqlconnection
import twostep

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
        if len(username) > 24:
            errormessage = 'De gebruikersnaam mag maximaal\n24 karakters lang zijn\nProbeer het nogmaals.'
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
        dataobject = { "username" : username, "password" : password, "secret" : twostep.GetSecret(), "storagestate" : "0", "storagedate" : "" }
        sqlconnection.CreateNewRow(sqlconn, sqlcursor, dataobject)

        return True, 'Het account\n{}\nis succesvol aangemaakt'.format(username)
    else:
        return False, errormessage