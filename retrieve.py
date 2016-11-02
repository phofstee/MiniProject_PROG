#auteur = Larsse Vink

import sqlconnection
import twostep

def RetrieveBike(uuid):
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()
    storagedate = ""

    userInfo = sqlconnection.GetRow(sqlcursor, {"uuid" : uuid})

    if userInfo[4] != 0:
        dataobject = { "storagestate" : "0", "storagedate" : storagedate }
        sqlconnection.UpdateRow(sqlconn, sqlcursor, dataobject, {"uuid" : uuid})
        return True, 'U kunt uw fiets ophalen.'
    else:
        return False, 'Uw fiets staat nog niet in de stalling.'