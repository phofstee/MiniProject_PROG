__author__ = "Pim Hofstee"

import sqlconnection
import datetime

def park(uuid):

    # settings for SQL connection
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()

    # username and password are match, update database
    # create storage date
    today = datetime.date.today()
    storagedate = today.strftime('%d-%m-%Y, %m:%m')

    dataobject = { "storagestate" : "1", "storagedate" : storagedate }
    #gebruik het sqlconn object als parameter, niet sqlconnection (het bestand)
    sqlconnection.UpdateRow(sqlconn, sqlcursor, dataobject, {"uuid" : uuid})

    # update succesfully
    print('')
    print('Login succesvol, u kunt uw fiets stallen.')