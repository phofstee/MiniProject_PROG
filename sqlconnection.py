__author__ = "Thomas"

import sqlite3

def InitializeSQL():
    sqlconnection = sqlite3.connect('stalling.db')
    sqlcursor = sqlconnection.cursor()
    sqlcursor.execute("CREATE TABLE IF NOT EXISTS stalling (uuid integer primary key autoincrement, username text, password text, secret text, storagestate integer, storagedate text)")

    return sqlconnection, sqlcursor

def CloseSQL(sqlconnection):
    sqlconnection.close()

def CreateNewRow(sqlconnection, sqlcursor, data):
    keystring = ""
    datastring = ""

    for key, value in data.items():
        keystring = keystring + ("{},".format(key))
        datastring = datastring + ("'{}',".format(value))

    keystring = keystring[:-1]
    datastring = datastring[:-1]

    sqlcursor.execute("INSERT INTO stalling ({}) VALUES ({})".format(keystring, datastring))
    sqlconnection.commit()

def UpdateRow(sqlconnection, sqlcursor, data, id):
    updatestring = ""
    key = ""
    value = ""

    for k, v in id.items():
        key = k
        value = v

    for k, v in data.items():
        updatestring = updatestring + ("{} = '{}',".format(k, v))

    updatestring = updatestring[:-1]

    sqlcursor.execute("UPDATE stalling SET {} WHERE {} = '{}'".format(updatestring, key, value))
    sqlconnection.commit()

def GetAllRows(sqlcursor):
    allrows = []

    for row in sqlcursor.execute("SELECT * FROM stalling"):
        allrows.append(row)

    return allrows

def GetRow(sqlcursor, id):
    data = None
    key = ""
    value = ""

    for k,v in id.items():
        key = k
        value = v

    for row in sqlcursor.execute("SELECT * FROM stalling WHERE {} = '{}'".format(key, value)):
        data = row

    return data