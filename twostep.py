__author__ = "Thomas"

import pyotp
import qrcode
import sqlconnection

def GetSecret():
    return pyotp.random_base32()

def GetTOTP(secret):
    totp = pyotp.TOTP(secret)
    totp.now()

    return totp.now()

def CreateAuthenticatorQRCode(secret, username):
    totp = pyotp.TOTP(secret)

    img = qrcode.make(totp.provisioning_uri("Fietsenstalling: {}".format(username)))
    img.save('qrcode.png')

def Authorize(authcode, uuid):
    sqlconn, sqlcursor = sqlconnection.InitializeSQL()

    if authcode == GetTOTP(sqlconnection.GetRow(sqlcursor, {"uuid" : uuid})[3]):
        return True
    else:
        return False