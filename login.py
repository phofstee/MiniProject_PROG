import sqlconnection
import menu

def login():
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    stallingData = sqlconnection.GetAllRows(sqlcursor)

    users = []
    accounts = []

    for row in stallingData:
        users.append(row[1])
        accounts.append([row[0], row[1], row[2]])

    print('Geef uw inloggegevens.')
    print('')

    # Voer gebruikersnaam in en test of deze voorkomt
    name = str.lower(input('Gebruikersnaam: '))
    while name not in users:
        print('Gebruiker komt niet voor in database. Probeer het nogmaals.')
        name = str.lower(input('Gebruikersnaam: '))

    # Voer wachtwoord in en kijk of deze klopt met het account
    for account in accounts:
        if account[1] == name:
            account_password = account[2]

    password = str(input('Wachtwoord:'))
    while account_password != password:
        print('Uw wachtwoord is onjuist. Probeer het nogmaals.')
        password = str(input('Wachtwoord:'))

    menu.menu()