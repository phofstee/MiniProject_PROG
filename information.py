__author__ = "Menno"

import sqlconnection

def ShowChoiceMenu(input, uuid):
    if input == "pers_info":
        sqlconn, sqlcursor = sqlconnection.InitializeSQL()
        return sqlconnection.GetRow(sqlcursor, {"uuid": uuid})
    if input == "gen_info":
        sqlconn, sqlcursor = sqlconnection.InitializeSQL()
        return len(sqlconnection.GetAllRows(sqlcursor))