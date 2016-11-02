__author__ = "Pim Hofstee"

import sqlconnection
import datetime

def ParkBike(uuid):
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()

    today = datetime.datetime.now()
    storagedate = today.strftime('%d-%m-%Y, %H:%M')

    userInfo = sqlconnection.GetRow(sqlcursor, {"uuid" : uuid})
    # Controleer of de fiets al gestald is of niet
    if userInfo[4] != 1:
        dataobject = { "storagestate" : "1", "storagedate" : storagedate }
        sqlconnection.UpdateRow(sqlconn, sqlcursor, dataobject, {"uuid" : uuid})
        return True, 'Uw fiets is gestald.'
    else:
        return False, 'Uw fiets staat nog in de stalling'