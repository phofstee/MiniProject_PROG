#auteur: Gijs

from tkinter import *
from tkinter.messagebox import showinfo
import login
import register
import sqlconnection
import retrieve
import information
import park

root = Tk()
root.configure(background='yellow')

#uuid global
uuid = None
mainmenu = None
choicewindow = None

def CenterWindow(rootobj):
    screen_width = rootobj.winfo_screenwidth() / 2
    screen_height = rootobj.winfo_screenheight() / 2
    rootobj.geometry("%dx%d+%d+%d" % (rootobj.winfo_reqwidth() if rootobj.winfo_reqwidth() > 400 else 450, rootobj.winfo_reqheight() if rootobj.winfo_reqheight() > 400 else 450 , (screen_width - (400 / 2)), (screen_height - ((400 / 2)))))

def ErrorWindow(windowtext):
    def close():
        global mainmenu
        if not mainmenu == None:
            mainmenu.deiconify()
        subwindow.destroy()

    subwindow = Toplevel(master=root)
    subwindow.configure(background='yellow')
    CenterWindow(subwindow)
    label = Label(master=subwindow, text=windowtext, background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    button1 = Button(master=subwindow, text='Sluiten', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=close)
    button1.pack(pady=10)

#login venster wordt aangeroepen
def toonVenster1():
    def close():
        subwindow.withdraw()

    def onEnter(event):
        username = entry1.get()
        password = entry2.get()

        result, data = login.AttemptLogin(username, password)

        if not result:
            if data == "username":
                ErrorWindow("Gebruikersnaam is onbekend")
            elif data == "password":
                ErrorWindow("Wachtwoord is onbekend")
        elif result:
            # door naar main menu
            global uuid
            uuid = data
            close()
            root.withdraw()
            sqlconn, sqlcursor = sqlconnection.InitializeSQL()
            ShowMainMenu(sqlconnection.GetRow(sqlcursor, {"uuid" : data})[1])

    subwindow = Toplevel(master=root)
    subwindow.configure(background='yellow')
    CenterWindow(subwindow)
    label = Label(master=subwindow, text='Vul hier uw login gegevens in', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    entry1 = Entry(master=subwindow, background='white')
    entry1.pack(pady=10, padx=10)
    entry1.bind('<Return>', onEnter)

    entry2 = Entry(master=subwindow, background='white')
    entry2.pack(pady=10, padx=10)
    entry2.bind('<Return>', onEnter)

#registreer venster wordt aangeroepen
def toonVenster2():
    def close():
        subwindow.withdraw()

    def onEnter(event):
        username = entry1.get()
        password = entry2.get()

        result, data = register.AttemptRegister(username, password)

        if not result:
            ErrorWindow(data)
        elif result:
            #door naar main menu
            ErrorWindow(data)
            result, data = login.AttemptLogin(username, password)
            if result:
                global uuid
                uuid = data
                close()
                root.withdraw()
                sqlconn, sqlcursor = sqlconnection.InitializeSQL()
                ShowMainMenu(sqlconnection.GetRow(sqlcursor, {"uuid": data})[1])

    subwindow = Toplevel(master=root)
    subwindow.configure(background='yellow')
    CenterWindow(subwindow)
    label = Label(master=subwindow, text='Vul hier uw gebruikersnaam en wachtwoord in', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    entry1 = Entry(master=subwindow, background='white')
    entry1.pack(pady=10, padx=10)
    entry1.bind('<Return>', onEnter)

    entry2 = Entry(master=subwindow, background='white')
    entry2.pack(pady=10, padx=10)
    entry2.bind('<Return>', onEnter)

def ChoiceWindow(windowtext, choices):
    global choicewindow
    def close():
        choicewindow.destroy()

    choicewindow = Toplevel(master=root)
    choicewindow.configure(background='yellow')
    CenterWindow(choicewindow)

    label = Label(master=choicewindow, text=windowtext, background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    for k,v in choices.items():
        argsButton = {k:k}
        button1 = Button(master=choicewindow, text=v, background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=lambda arg=argsButton: RunAction(arg))
        button1.pack(pady=10)

def LabelWindow(windowtext, labels):
    def close():
        global mainmenu
        mainmenu.deiconify()
        subwindow.destroy()

    subwindow = Toplevel(master=root)
    CenterWindow(subwindow)
    subwindow.configure(background='yellow')
    label = Label(master=subwindow, text=windowtext, background='blue', foreground='white',font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    for k,v in labels.items():
        label1 = Label(master=subwindow, text=v, background='yellow', foreground='black', font=('Calibri', 11, 'bold'))
        label1.pack(pady=10)

    button1 = Button(master=subwindow, text='Sluiten', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=close)
    button1.pack(pady=10)

def RunAction(args):
    global uuid
    global mainmenu

    for k, v in args.items():
        if v == "park":
            succes, result = park.ParkBike(uuid)
            ErrorWindow(result)
        if v == "retrieve":
            succes, result = retrieve.RetrieveBike(uuid)
            ErrorWindow(result)
        if v == "info":
            #succes, result = information.ShowChoiceMenu(uuid)
            ChoiceWindow("Maak een Keuze", {"pers_info" : "Persoonlijke informatie", "gen_info" : "Algemene informatie"})
            mainmenu.withdraw()
            #ErrorWindow(result)
        if v == "logout":
            mainmenu.destroy()
            mainmenu = None
            root.deiconify()
            uuid = None
        if v == "gen_info":
            choicewindow.destroy()
            result = information.ShowChoiceMenu(v, uuid)
            ErrorWindow('Er zijn in totaal {} gebruikers.'.format(result))
        if v == "pers_info":
            choicewindow.destroy()
            result = information.ShowChoiceMenu(v, uuid)
            LabelWindow("Persoonlijke Informatie:",
            {
                "uuid" : "Gebruikers-ID: {}".format(result[0]),
                "username" : "Gebruikersnaam: {}".format(result[1]),
                "storagestate" : "Fiets in stalling: {}".format('Ja' if result[4] == 1 else 'Nee'),
                "storagedate" : "Datum en tijd van stalling: {}".format(result[5])
            })

def ShowMainMenu(username):
    # auteur: Gijs
    global mainmenu
    mainmenu = Tk()
    mainmenu.configure(background='yellow')
    CenterWindow(mainmenu)

    # label
    label = Label(master=mainmenu, text='Welkom, {}'.format(username), background='blue', foreground='white',font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    # Fiets stallen
    argsButton1 = {"action" : "park"}
    button1 = Button(master=mainmenu, text='Fiets stallen', background='blue', foreground='white',font=('Calibri', 11, 'bold'), command=lambda arg=argsButton1: RunAction(arg))
    button1.pack(pady=10)

    # Informatie opvragen
    argsButton2 = {"action" : "info"}
    button2 = Button(master=mainmenu, text='Informatie opvragen', background='blue', foreground='white',font=('Calibri', 11, 'bold'), command=lambda arg=argsButton2: RunAction(arg))
    button2.pack(pady=10)

    # Fiets ophalen
    argsButton3 = {"action": "retrieve"}
    button3 = Button(master=mainmenu, text='Fiets ophalen', background='blue', foreground='white',font=('Calibri', 11, 'bold'), command=lambda arg=argsButton3: RunAction(arg))
    button3.pack(pady=10)

    # Uitloggen
    argsButton4 = {"action": "logout"}
    button4 = Button(master=mainmenu, text='Uitloggen', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=lambda arg=argsButton4: RunAction(arg))
    button4.pack(pady=10)

    mainmenu.mainloop()

#label
label = Label(master=root, text='Welkom bij de NS-fietsenstalling', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
label.pack()

#login button
button1 = Button(master=root, text='Login', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=toonVenster1)
button1.pack(pady=10)

#registreer button
button2 = Button(master=root, text='Registreer', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=toonVenster2)
button2.pack(pady=10)

CenterWindow(root)

root.mainloop()
