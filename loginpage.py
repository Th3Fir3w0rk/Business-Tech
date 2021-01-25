import tkinter as tk
from tkinter import *
import tkinter.messagebox as tm
import sqlite3
import os

def verif():
	ident = ID.get()
	passw = MDP.get()
	db = sqlite3.connect('Database/database.db')
	cursor = db.cursor()
	cursor.execute('SELECT id FROM login')
	user_list = cursor.fetchall()
	cursor.execute('SELECT mdp FROM login')
	user_mdp = cursor.fetchall()

	for i in user_list:
		if ident in i:
			if ident == 'admin':
				for m in user_mdp:
					if passw in m:
						PASS = ("'" + ID.get() + "'")
						cursor.execute("SELECT * FROM login WHERE id = " + PASS)
						iid = cursor.fetchone()[0]
						cursor.execute("SELECT * FROM login WHERE id = " + PASS)
						first = cursor.fetchone()[1]
						cursor.execute("SELECT * FROM login WHERE id = " + PASS)
						last = cursor.fetchone()[2]
						user = sqlite3.connect('Database/user_database.db')
						cur = user.cursor()
						cur.execute('CREATE TABLE IF NOT EXISTS us_er (id TEXT, first_name TEXT, last_name TEXT)')
						cur.execute('INSERT INTO us_er VALUES (:id, :first_name, :last_name)',
							{
								'id':''+iid,
								'first_name':''+first,
								'last_name':''+last
							})
						user.commit()
						user.close()
						window.destroy()
						os.system("python admin.py")
			else:
				for m in user_mdp:
					if passw in m:
						PASS = ("'" + ID.get() + "'")
						cursor.execute("SELECT * FROM login WHERE id = " + PASS)
						iid = cursor.fetchone()[0]
						cursor.execute("SELECT * FROM login WHERE id = " + PASS)
						first = cursor.fetchone()[1]
						cursor.execute("SELECT * FROM login WHERE id = " + PASS)
						last = cursor.fetchone()[2]
						user = sqlite3.connect('Database/user_database.db')
						cur = user.cursor()
						cur.execute('CREATE TABLE IF NOT EXISTS us_er (id TEXT, first_name TEXT, last_name TEXT)')
						cur.execute('INSERT INTO us_er VALUES (:id, :first_name, :last_name)',
							{
								'id':''+iid,
								'first_name':''+first,
								'last_name':''+last
							})
						user.commit()
						user.close()
						window.destroy()
						os.system("python user.py")

window = tk.Tk()
window.title('BusinessTech')
window.geometry('1280x720')
window.resizable(width=False, height=False)
icon = tk.PhotoImage(file='Image/bt.gif')
window.iconphoto(True, icon)
window.configure(background='#013D6B')

space = Frame(window, bg='#013D6B')
conn = Frame(window, bg='#013D6B')
logg = Frame(window, bg='#013D6B')
logg_in = Frame(window, bg='#013D6B')
space.grid(column=0, row=0, padx=510, pady=140)
conn.grid(column=0, row=1, padx=510)
logg.grid(column=0, row=2, padx=510)
logg_in.grid(column=0, row=3, padx=510)

label = Label(conn, text='CONNEXION', font=('Arial', 20), bg='white', fg='#013D6B')
label_ID = Label(logg, text='ID -->', font=('Arial', 9), bg='white', fg='black')
label_MDP = Label(logg, text='MDP --> ', font=('Arial', 9), bg='white', fg='black')
label.grid(ipadx=52, ipady=5, pady=4)
label_ID.grid(row=0, column=0, ipadx=9, padx=2)
label_MDP.grid(row=1, column=0, padx=2)

ID = StringVar()
entry_ID = Entry(logg, textvariable=ID, width=30, bg='white')
entry_ID.grid(row=0, column=1)
MDP = StringVar()
entry_MDP = Entry(logg, textvariable=MDP, show='*', width=30)
entry_MDP.grid(row=1, column=1)
Button = Button(logg_in, text='LOGIN', command=verif)
Button.grid(row=2, column=1, ipadx=60, pady=15)

window.mainloop()