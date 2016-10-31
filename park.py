__author__ = "Pim Hofstee"

import sqlconnection
import datetime

def park():

    # settings for SQL connection
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    stallingData = sqlconnection.GetAllRows(sqlcursor)

    users = []
    accounts = []

    for row in stallingData:
        users.append(row[1])
        accounts.append([row[0], row[1], row[2]])

    print('Voordat u uw fiets kunt stallen, moet u eerst inloggen.')
    print('')

    # Enter username and check if username exists
    name = str.lower(input('Gebruikersnaam: '))
    while name not in users:
        print('Gebruiker komt niet voor in database. Probeer het nogmaals.')
        name = str.lower(input('Gebruikersnaam: '))

    # Enter password and check if password does match
    for account in accounts:
        if account[1] == name:
            account_password = account[2]

    password = str(input('Wachtwoord:'))
    while account_password != password:
        print('Uw wachtwoord is onjuist. Probeer het nogmaals.')
        password = str(input('Wachtwoord:'))

    # username and password are match, update database
    # create storage date
    today = datetime.date.today()
    storagedate = today.strftime('%d-%m-%Y, %m:%m')

    dataobject = { "username" : name, "password" : password, "storagestate" : "1", "storagedate" : storagedate }
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    sqlconnection.UpdateRow(sqlconnection, sqlcursor, dataobject, {"uuid" : account[0]})

    # update succesfully
    print('')
    print('Login succesvol, u kunt uw fiets stallen.')

park()