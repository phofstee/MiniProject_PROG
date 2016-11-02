__author__ = "Pim"

import sqlconnection

def AttemptLogin(username, password):
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    stallingData = sqlconnection.GetAllRows(sqlcursor)

    # Maak een lijst van alle users, om later mee te checken
    users = []
    accounts = []
    account_uuid = None
    account_password = None

    # Voer gebruikersnaam in en test of deze voorkomt
    for row in stallingData:
        users.append(row[1])
        accounts.append([row[0], row[1], row[2]])

    if username not in users:
        return False, "username"

    # Voer wachtwoord in en check of deze voorkomt
    for account in accounts:
        if account[1] == username:
            account_uuid = account[0]
            account_password = account[2]

    if account_password != password:
        return False, "password"

    if username in users and account_password == password:
        return True, account_uuid