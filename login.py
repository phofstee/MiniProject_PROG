__author__ = "Pim"

import sqlconnection

def AttemptLogin(username, password):
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    stallingData = sqlconnection.GetAllRows(sqlcursor)

    users = []
    accounts = []
    account_uuid = None

    account_password = None

    for row in stallingData:
        users.append(row[1])
        accounts.append([row[0], row[1], row[2]])

    # Voer gebruikersnaam in en test of deze voorkomt
    if username not in users:
        return False, "username"

    for account in accounts:
        if account[1] == username:
            account_uuid = account[0]
            account_password = account[2]

    if account_password != password:
        return False, "password"

    if username in users and account_password == password:
        return True, account_uuid