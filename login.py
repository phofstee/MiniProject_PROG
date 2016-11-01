import sqlconnection
import time

def login():
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    stallingData = sqlconnection.GetAllRows(sqlcursor)

    users = []
    accounts = []
    account_uuid = None
    user_login_attempts = 0
    password_login_attempts = 0

    for row in stallingData:
        users.append(row[1])
        accounts.append([row[0], row[1], row[2]])

    print('Geef uw inloggegevens.')

    # Voer gebruikersnaam in en test of deze voorkomt
    name = str.lower(input('Gebruikersnaam: '))
    while name not in users and user_login_attempts < 2:
        user_login_attempts = user_login_attempts + 1
        print('Gebruiker komt niet voor in database. Probeer het nogmaals.')
        name = str.lower(input('Gebruikersnaam: '))

    if user_login_attempts < 2:
        # Voer wachtwoord in en kijk of deze klopt met het account
        for account in accounts:
            if account[1] == name:
                account_uuid = account[0]
                account_password = account[2]

            password = str(input('Wachtwoord: '))
        while account_password != password and password_login_attempts < 2 and user_login_attempts != 2:
            password_login_attempts = password_login_attempts + 1
            print('Uw wachtwoord is onjuist. Probeer het nogmaals.')
            password = str(input('Wachtwoord: '))

        if user_login_attempts < 2 or password_login_attempts < 2:
            print('U heeft te vaak geprobeerd in te loggen, u wordt terug gestuurd naar het menu.')
            time.sleep(2)

        return True, account_uuid