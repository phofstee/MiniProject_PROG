__author__ = "Menno"

import sqlconnection

def ShowChoiceMenu(input, uuid):
    # haal info op van de gebruiker
    if input == "pers_info":
        sqlconn, sqlcursor = sqlconnection.InitializeSQL()
        return sqlconnection.GetRow(sqlcursor, {"uuid": uuid})

    # haal alle info op uit de DB
    if input == "gen_info":
        sqlconn, sqlcursor = sqlconnection.InitializeSQL()
        return len(sqlconnection.GetAllRows(sqlcursor))