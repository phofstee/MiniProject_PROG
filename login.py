#auteur: Gijs

from tkinter import *
from tkinter.messagebox import showinfo

#login venster wordt aangeroepen
def toonVenster1():
    def close():
        subwindow.withdraw()

    subwindow = Toplevel(master=root)
    label = Label(master=subwindow, text='Vul hier uw login gegevens in', background='yellow', foreground='blue', font=('Times New Roman', 16, 'bold'), width=40, height=3)
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
    label = Label(master=subwindow, text='Vul hier uw gebruikersnaam en wachtwoord in', background='yellow', foreground='blue', font=('Times New Roman', 16, 'bold'), width=40, height=3)
    label.pack()

    entry1 = Entry(master=subwindow, background='white')
    entry1.pack(pady=10, padx=10)

    entry2 = Entry(master=subwindow, background='white')
    entry2.pack(pady=10, padx=10)


root = Tk()

#label
label = Label(master=root, text='Welkom bij de NS-fietsenstalling', background='yellow', foreground='blue', font=('Times New Roman', 16, 'bold'), width=40, height=3)
label.pack()

#login button
button1 = Button(master=root, text='Login', background='yellow', foreground='black', font=('Times New Roman', 11, 'bold'), command=toonVenster1)
button1.pack(pady=10)

#registreer button
button2 = Button(master=root, text='Registreer', background='yellow', foreground='black', font=('Times New Roman', 11, 'bold'), command=toonVenster2)
button2.pack(pady=10)

root.mainloop()
