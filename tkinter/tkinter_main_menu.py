#auteur: Gijs

from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()
root.configure(background='yellow')

#label
label = Label(master=root, text='Welkom, [NAAM]', background='blue', foreground='white', font=('Calibri', 16, 'bold'), width=40, height=3)
label.pack()

#Fiets stallen
button1 = Button(master=root, text='Fiets stallen', background='blue', foreground='white', font=('Calibri', 11, 'bold'))
button1.pack(pady=10)

#Informatie opvragen
button2 = Button(master=root, text='Informatie opvragen', background='blue', foreground='white', font=('Calibri', 11, 'bold'))
button2.pack(pady=10)

#Fiets ophalen
button3 = Button(master=root, text='Fiets ophalen', background='blue', foreground='white', font=('Calibri', 11, 'bold'))
button3.pack(pady=10)

#Uitloggen
button4 = Button(master=root, text='Uitloggen', background='blue', foreground='white', font=('Calibri', 11, 'bold'))
button4.pack(pady=10)

root.mainloop()
