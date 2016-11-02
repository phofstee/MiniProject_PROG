__author__ = "Menno Noltes"
__version__ = 1.0
__status__ = 'Development'

import sqlconnection

def ShowChoiceMenu(input, uuid):
    if input == "pers_info":
        sqlconn, sqlcursor = sqlconnection.InitializeSQL()
        return sqlconnection.GetRow(sqlcursor, {"uuid": uuid})
    if input == "gen_info":
        sqlconn, sqlcursor = sqlconnection.InitializeSQL()
        return len(sqlconnection.GetAllRows(sqlcursor))