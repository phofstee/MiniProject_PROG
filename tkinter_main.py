__author__ = "Thomas, Gijs, Larsse, Menno, Pim"

import tkinter
import login
import register
import sqlconnection
import retrieve
import information
import park
import twostep

__author__ = "Thomas"
def CenterWindow(rootobj, width=450, height=450):
    screen_width = (rootobj.winfo_screenwidth() / 2)
    screen_height = (rootobj.winfo_screenheight() / 2)
    rootobj.geometry("%dx%d+%d+%d" % (width, height, (screen_width - (width / 2)), (screen_height - ((height / 2)))))

__author__ = "Thomas"
def PopupWindow(windowtext):
    def close():
        global mainmenu
        if not mainmenu == None:
            mainmenu.deiconify()
        subwindow.destroy()

    subwindow = tkinter.Toplevel(master=root)
    subwindow.configure(background='yellow')
    CenterWindow(subwindow)
    label = tkinter.Label(master=subwindow, text=windowtext, background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    button1 = tkinter.Button(master=subwindow, text='Sluiten', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=close)
    button1.pack(pady=10)

__author__ = "Thomas"
def AfterRegisterWindow(windowtext):
    def close():
        global mainmenu
        if not mainmenu == None:
            mainmenu.deiconify()
        subwindow.destroy()

    subwindow = tkinter.Toplevel(master=root)
    subwindow.configure(background='yellow')

    label = tkinter.Label(master=subwindow, text=windowtext, background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    qrcodeImage = tkinter.PhotoImage(file="qrcode.png")
    qrcodeImageLabel = tkinter.Label(subwindow, image=qrcodeImage)
    qrcodeImageLabel.photo = qrcodeImage
    qrcodeImageLabel.pack()

    button1 = tkinter.Button(master=subwindow, text='Sluiten', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=close)
    button1.pack(pady=10)

    CenterWindow(subwindow, 450, 700)

#login venster wordt aangeroepen
__author__ = "Gijs, Thomas"
def LoginScreen():
    def close():
        subwindow.destroy()

    def onEnter(event):
        username = entry1.get()
        password = entry2.get()

        result, data = login.AttemptLogin(username, password)

        if not result:
            if data == "username":
                PopupWindow("Gebruikersnaam is onbekend")
            elif data == "password":
                PopupWindow("Wachtwoord is onbekend")
        elif result:
            global uuid
            uuid = data

            close()
            root.withdraw()

            sqlconn, sqlcursor = sqlconnection.InitializeSQL()
            ShowMainMenu(sqlconnection.GetRow(sqlcursor, {"uuid" : data})[1])

    subwindow = tkinter.Toplevel(master=root)
    subwindow.configure(background='yellow')
    CenterWindow(subwindow)
    label = tkinter.Label(master=subwindow, text='Vul hier uw login gegevens in', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    entry1 = tkinter.Entry(master=subwindow, background='white')
    entry1.pack(pady=10, padx=10)
    entry1.bind('<Return>', onEnter)

    entry2 = tkinter.Entry(master=subwindow, background='white')
    entry2.pack(pady=10, padx=10)
    entry2.bind('<Return>', onEnter)

    button1 = tkinter.Button(master=subwindow, text='Sluiten', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=close)
    button1.pack(pady=10)

__author__ = "Thomas"
def AuthCodeWindow():
    global uuid
    global mainmenu

    def close():
        mainmenu.deiconify()
        subwindow.destroy()

    def onEnter(event):
        authcode = entry1.get()

        if twostep.Authorize(authcode, uuid):
            succes, result = retrieve.RetrieveBike(uuid)
            PopupWindow(result)
            close()
        else:
            PopupWindow("Foute Authenticatiecode")
            close()

    subwindow = tkinter.Toplevel(master=root)
    subwindow.configure(background='yellow')

    CenterWindow(subwindow)
    label = tkinter.Label(master=subwindow, text='Vul hier uw authenticatiecode in', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    entry1 = tkinter.Entry(master=subwindow, background='white')
    entry1.pack(pady=10, padx=10)
    entry1.bind('<Return>', onEnter)

    button1 = tkinter.Button(master=subwindow, text='Sluiten', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=close)
    button1.pack(pady=10)

#registreer venster wordt aangeroepen
__author__ = "Gijs, Thomas"
def RegisterScreen():
    def close():
        subwindow.destroy()

    def onEnter(event):
        username = entry1.get()
        password = entry2.get()

        result, data = register.AttemptRegister(username, password)

        if not result:
            PopupWindow(data)
        elif result:
            sqlconn, sqlcursor = sqlconnection.InitializeSQL()
            userData = sqlconnection.GetRow(sqlcursor, {"username": username})
            twostep.CreateAuthenticatorQRCode(userData[3], userData[1])
            AfterRegisterWindow("Scan de QR Code met de\nGoogle Authenticator app")

            result, data = login.AttemptLogin(username, password)
            if result:
                global uuid
                uuid = data
                close()
                root.withdraw()

                ShowMainMenu(userData[1])

    subwindow = tkinter.Toplevel(master=root)
    subwindow.configure(background='yellow')
    CenterWindow(subwindow)
    label = tkinter.Label(master=subwindow, text='Vul hier uw gebruikersnaam en wachtwoord in', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    entry1 = tkinter.Entry(master=subwindow, background='white')
    entry1.pack(pady=10, padx=10)
    entry1.bind('<Return>', onEnter)

    entry2 = tkinter.Entry(master=subwindow, background='white')
    entry2.pack(pady=10, padx=10)
    entry2.bind('<Return>', onEnter)

    button1 = tkinter.Button(master=subwindow, text='Sluiten', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=close)
    button1.pack(pady=10)

__author__ = "Thomas"
def ChoiceWindow(windowtext, choices):
    global choicewindow
    def close():
        choicewindow.destroy()

    choicewindow = tkinter.Toplevel(master=root)
    choicewindow.configure(background='yellow')
    CenterWindow(choicewindow)

    label = tkinter.Label(master=choicewindow, text=windowtext, background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    for k,v in choices.items():
        argsButton = {k:k}
        button1 = tkinter.Button(master=choicewindow, text=v, background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=lambda arg=argsButton: RunAction(arg))
        button1.pack(pady=10)

__author__ = "Thomas"
def LabelWindow(windowtext, labels):
    def close():
        global mainmenu
        mainmenu.deiconify()
        subwindow.destroy()

    subwindow = tkinter.Toplevel(master=root)
    CenterWindow(subwindow)
    subwindow.configure(background='yellow')
    label = tkinter.Label(master=subwindow, text=windowtext, background='blue', foreground='white',font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    for k,v in labels.items():
        label1 = tkinter.Label(master=subwindow, text=v, background='yellow', foreground='black', font=('Calibri', 11, 'bold'))
        label1.pack(pady=10)

    button1 = tkinter.Button(master=subwindow, text='Sluiten', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=close)
    button1.pack(pady=10)

__author__ = "Thomas, Larsse, Pim, Menno"
def RunAction(args):
    global uuid
    global mainmenu

    for k, v in args.items():
        if v == "park":
            succes, result = park.ParkBike(uuid)
            PopupWindow(result)
        if v == "retrieve":
            AuthCodeWindow()
            mainmenu.withdraw()
        if v == "info":
            ChoiceWindow("Maak een Keuze", {"pers_info" : "Persoonlijke informatie", "gen_info" : "Algemene informatie"})
            mainmenu.withdraw()
        if v == "logout":
            mainmenu.destroy()
            mainmenu = None
            root.deiconify()
            uuid = None
        if v == "gen_info":
            choicewindow.destroy()
            result = information.ShowChoiceMenu(v, uuid)
            PopupWindow('Er zijn in totaal {} gebruikers.'.format(result))
        if v == "pers_info":
            choicewindow.destroy()
            result = information.ShowChoiceMenu(v, uuid)
            LabelWindow("Persoonlijke Informatie:",
            {
                "uuid" : "Gebruikers-ID: {}".format(result[0]),
                "username" : "Gebruikersnaam: {}".format(result[1]),
                "storagestate" : "Fiets in stalling: {}".format('Ja' if result[4] == 1 else 'Nee'),
                "storagedate" : "Datum en tijd van stalling: {}".format(result[5] if result[5] != "" else 'Geen fiets gestald')
            })

__author__ = "Gijs, Thomas, Pim, Menno, Larsse"
def ShowMainMenu(username):
    global mainmenu
    mainmenu = tkinter.Tk()
    mainmenu.configure(background='yellow')
    CenterWindow(mainmenu)

    # Welkom label
    label = tkinter.Label(master=mainmenu, text='Welkom, {}'.format(username), background='blue', foreground='white',font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    # Fiets stallen
    argsButton1 = {"action" : "park"}
    button1 = tkinter.Button(master=mainmenu, text='Fiets stallen', background='blue', foreground='white',font=('Calibri', 11, 'bold'), command=lambda arg=argsButton1: RunAction(arg))
    button1.pack(pady=10)

    # Informatie opvragen
    argsButton2 = {"action" : "info"}
    button2 = tkinter.Button(master=mainmenu, text='Informatie opvragen', background='blue', foreground='white',font=('Calibri', 11, 'bold'), command=lambda arg=argsButton2: RunAction(arg))
    button2.pack(pady=10)

    # Fiets ophalen
    argsButton3 = {"action": "retrieve"}
    button3 = tkinter.Button(master=mainmenu, text='Fiets ophalen', background='blue', foreground='white',font=('Calibri', 11, 'bold'), command=lambda arg=argsButton3: RunAction(arg))
    button3.pack(pady=10)

    # Uitloggen
    argsButton4 = {"action": "logout"}
    button4 = tkinter.Button(master=mainmenu, text='Uitloggen', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=lambda arg=argsButton4: RunAction(arg))
    button4.pack(pady=10)

    mainmenu.mainloop()

uuid = None
mainmenu = None
choicewindow = None

if __name__ == "__main__":
    root = tkinter.Tk()
    root.configure(background='yellow')

    #label
    label = tkinter.Label(master=root, text='Welkom bij de NS-fietsenstalling', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    #login button
    button1 = tkinter.Button(master=root, text='Login', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=LoginScreen)
    button1.pack(pady=10)

    #registreer button
    button2 = tkinter.Button(master=root, text='Registreer', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=RegisterScreen)
    button2.pack(pady=10)

    CenterWindow(root)

    root.mainloop()