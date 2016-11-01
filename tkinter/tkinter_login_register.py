#auteur: Gijs

from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.configure(background='yellow')

#login venster wordt aangeroepen
def toonVenster1():
    def close():
        subwindow.withdraw()
    subwindow = Toplevel(master=root)
    subwindow.configure(background='yellow')
    label = Label(master=subwindow, text='Vul hier uw login gegevens in', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    entry1 = Entry(master=subwindow, background='white')
    entry1.pack(pady=10, padx=10)

    entry2 = Entry(master=subwindow, background='white')
    entry2.pack(pady=10, padx=10)

#registreer venster wordt aangeroepen
def toonVenster2():
    def close():
        subwindow.withdraw()
    subwindow = Toplevel(master=root)
    subwindow.configure(background='yellow')
    label = Label(master=subwindow, text='Vul hier uw gebruikersnaam en wachtwoord in', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
    label.pack()

    entry1 = Entry(master=subwindow, background='white')
    entry1.pack(pady=10, padx=10)

    entry2 = Entry(master=subwindow, background='white')
    entry2.pack(pady=10, padx=10)


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
