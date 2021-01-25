import tkinter as tk
from tkinter import *
import tkinter.messagebox as tm
import sqlite3

def new_user():
	db = sqlite3.connect('Database/database.db')
	cursor = db.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS login (id TEXT, first_name TEXT, last_name TEXT, email TEXT, mdp TEXT)')
	cursor.execute('INSERT INTO login VALUES (:id, :first_name, :last_name, :email, :mdp)',
		{
			'id':ID.get(),
			'first_name':FIRST_NAME.get(),
			'last_name':LAST_NAME.get(),
			'email':EMAIL.get(),
			'mdp':MDP.get()
		})
	db.commit()
	db.close()
	window.destroy()

window = tk.Tk()
window.title('BusinessTech')
window.geometry('230x160')
window.resizable(width=False, height=False)
icon = tk.PhotoImage(file='Image/bt.gif')
window.iconphoto(True, icon)

ID = StringVar()
ID.set('IDENTIFIANT')
entry_ID = Entry(window, textvariable=ID, width=30, bg='white')
entry_ID.pack(pady=2)
FIRST_NAME = StringVar()
FIRST_NAME.set('Prénom')
entry_FIRST_NAME = Entry(window, textvariable=FIRST_NAME, width=30, bg='white')
entry_FIRST_NAME.pack(pady=2)
LAST_NAME = StringVar()
LAST_NAME.set('Nom')
entry_LAST_NAME = Entry(window, textvariable=LAST_NAME, width=30, bg='white')
entry_LAST_NAME.pack(pady=2)
EMAIL = StringVar()
EMAIL.set('Email')
entry_EMAIL = Entry(window, textvariable=EMAIL, width=30, bg='white')
entry_EMAIL.pack(pady=2)
MDP = StringVar()
MDP.set('Mot de Passe')
entry_MDP = Entry(window, textvariable=MDP, width=30)
entry_MDP.pack()
Button = Button(window, text='NEW USER', command=new_user)
Button.pack(pady=10)

window.mainloop()