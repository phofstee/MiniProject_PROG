__author__ = "Pim Hofstee"

import sqlconnection
import datetime

def park():

    # settings for SQL connection
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()


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