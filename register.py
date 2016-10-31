import datetime
import sqlconnection

def register():
    print('We gaan uw fiets nu registeren')
    name = str(input('Geef uw gebruikersnaam op: '))
    password = str(input('Geef uw wachtwoord op: '))
    today = datetime.date.today()
    storagedate = today.strftime('%d-%m-%Y, %H:%m')

    dataobject = { "username" : name, "password" : password, "storagestate" : "0", "storagedate" : storagedate }
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    sqlconnection.CreateNewRow(sqlconn, sqlcursor, dataobject)
    print(sqlconnection.GetAllRows(sqlcursor))

register()