#auteur: Gijs

from tkinter import *
from tkinter.messagebox import showinfo
import login
import register

root = Tk()
root.configure(background='yellow')

def ErrorWindow(windowtext):
    def close():
        subwindow.withdraw()

    subwindow = Toplevel(master=root)
    subwindow.configure(background='yellow')
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

        print(result, data)

        if not result:
            if data == "username":
                ErrorWindow("Gebruikersnaam is onbekend")
            elif data == "password":
                ErrorWindow("Wachtwoord is onbekend")
        elif result:
            # door naar main menu
            None

    subwindow = Toplevel(master=root)
    subwindow.configure(background='yellow')
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

    subwindow = Toplevel(master=root)
    subwindow.configure(background='yellow')
    label = Label(master=subwindow, text='Vul hier uw gebruikersnaam en wachtwoord in', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    entry1 = Entry(master=subwindow, background='white')
    entry1.pack(pady=10, padx=10)
    entry1.bind('<Return>', onEnter)

    entry2 = Entry(master=subwindow, background='white')
    entry2.pack(pady=10, padx=10)
    entry2.bind('<Return>', onEnter)

#label
label = Label(master=root, text='Welkom bij de NS-fietsenstalling', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
label.pack()

#login button
button1 = Button(master=root, text='Login', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=toonVenster1)
button1.pack(pady=10)

#registreer button
button2 = Button(master=root, text='Registreer', background='blue', foreground='white', font=('Calibri', 11, 'bold'), command=toonVenster2)
button2.pack(pady=10)

root.mainloop()
