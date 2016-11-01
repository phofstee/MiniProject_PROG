#pip install pyotp
#pip install qrcode
#pip install pillow

import time
import pyotp
import qrcode
from PIL import Image

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
    img = Image.open('qrcode.png')
    img.show()

    while(True):
        print(GetTOTP(secret))
        time.sleep(1)

    return secret

CreateAuthenticatorQRCode(GetSecret(), "Thomas Korevaar")