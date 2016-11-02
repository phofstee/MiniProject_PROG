__author__ = "Larsse"

import sqlconnection
import twostep

def RetrieveBike(uuid):
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    storagedate = ""

    # haal user info op
    userInfo = sqlconnection.GetRow(sqlcursor, {"uuid" : uuid})

    # Pas data aan, en sla deze op, indien de fiets daadwerkelijk in de stalling staat
    if userInfo[4] != 0:
        dataobject = { "storagestate" : "0", "storagedate" : storagedate }
        sqlconnection.UpdateRow(sqlconn, sqlcursor, dataobject, {"uuid" : uuid})
        return True, 'U kunt uw fiets ophalen.'
    else:
        return False, 'Uw fiets staat nog niet in de stalling.'