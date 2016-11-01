__author__ = "Pim Hofstee"

import sqlconnection
import datetime

def park(uuid):

    # settings for SQL connection
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()

    # username and password are match, update database
    # create storage date
    today = datetime.date.today()
    storagedate = today.strftime('%d-%m-%Y, %H:%M')

    userInfo = sqlconnection.GetRow(sqlcursor, {"uuid" : uuid})
    print()
    # Controleer of de fiets al gestald is of niet
    if userInfo[3] != 1:
        dataobject = { "storagestate" : "1", "storagedate" : storagedate }
        sqlconnection.UpdateRow(sqlconn, sqlcursor, dataobject, {"uuid" : uuid})
        print('Uw fiets is gestald.')
    else:
        print('Uw fiets staat nog in de stalling')