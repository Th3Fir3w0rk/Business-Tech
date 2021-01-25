from tkinter import*
from tkcalendar import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter.messagebox as tm
from datetime import datetime, timedelta
import sqlite3
import time
import os

def logout():
	user = sqlite3.connect('Database/user_database.db')
	cur = user.cursor()

	time_logout = time.strftime('%H:%M:%S')
	datetime_logout = datetime.strptime(time_logout, '%H:%M:%S')
	datetime_travail = datetime_logout - datetime_login
	time_travail = str((datetime_travail))
	cursor_temp.execute('''INSERT INTO temp (pseudo_temp, jour, heure_login, heure_logout, heure_travail)
	VALUES (?, ?, ?, ?, ?)''',(pseudo, jour_login, time_login, time_logout, time_travail))
	db_temp.commit()
	cur.execute('DELETE FROM us_er')
	user.commit()
	user.close()
	window.destroy()
	os.system('python loginpage.py')

def destroy_window():
	for w in frame_accueil.winfo_children():
		w.destroy()
		frame_accueil.grid_forget()
	for x in frame_planning.winfo_children():
		x.destroy()
		frame_planning.grid_forget()
	for y in frame_communication.winfo_children():
		y.destroy()
		frame_communication.grid_forget()
	for z in frame_salaire.winfo_children():
		z.destroy()
		frame_salaire.grid_forget()

def accueil():
	destroy_window()
	frame_accueil.grid()
	#code here :

def planning():
	destroy_window()
	frame_planning.grid()
	#code here :

	def is_pressed():
		planning_db = sqlite3.connect('Database/planning.db')
		c_planning = planning_db.cursor()
		c_planning.execute('CREATE TABLE IF NOT EXISTS t_plan (user TEXT, date TEXT, note TEXT)')
		c_planning.execute('INSERT INTO t_plan VALUES (:user, :date, :note)',
			{
				'user':current_user,
				'date':calendar.get_date(),
				'note':entry_taches.get()
			})
		planning_db.commit()
		planning_db.close()
		planning()

	left_frame = Frame(frame_planning)
	right_frame = Frame(frame_planning, bg='#4d4d4d')
	left_frame.grid(column=0, row=1, sticky=W, padx=15, pady=10)
	right_frame.grid(column=1, row=1, sticky=W, padx=10)
	frame_taches = Frame(right_frame, bg="white")
	frame_taches.grid(row=4, ipadx=180, ipady=220)
	frame_taches.grid_propagate(0)

	user = sqlite3.connect('Database/user_database.db')
	cur = user.cursor()
	cur.execute('SELECT * FROM us_er')
	current_user = cur.fetchone()[0]
	current_admin = 'admin'

	calendar = Calendar(left_frame, selectmode='day')
	calendar.grid(ipadx=300, ipady=240)
	bt_get_date = Button(right_frame, command=is_pressed, bg='#4d4d4d', highlightthickness=0, bd=0)
	bt_get_date.grid(row=5, ipadx=165)

	planning_db = sqlite3.connect('Database/planning.db')
	c_planning = planning_db.cursor()
	TT = ("'" + current_user + "'")
	AA = ("'" + current_admin + "'")
	c_planning.execute("SELECT date, note FROM t_plan WHERE user =" + TT)
	date_db = c_planning.fetchall()
	c_planning.execute("SELECT date, note FROM t_plan WHERE user =" + AA)
	date_ad = c_planning.fetchall()
	
	date=''
	for db in date_db:
		origin = str(db)
		rm_comma = origin.replace(",", " : ")
		rm_quotes = rm_comma.replace("'", "")
		rm_par1 = rm_quotes.replace("(", "")
		rm_par2 = rm_par1.replace(")", "")
		date += rm_par2 + '\n'

	data=''
	for ad in date_ad:
		origin = str(ad)
		rm_comma = origin.replace(",", " : ")
		rm_quotes = rm_comma.replace("'", "")
		rm_par1 = rm_quotes.replace("(", "")
		rm_par2 = rm_par1.replace(")", "")
		data += rm_par2 + '\n'

	horaires = sqlite3.connect('Database/horaires.db')
	c_horaires = horaires.cursor()
	c_horaires.execute('SELECT * FROM t_hor')
	act_user = c_horaires.fetchone()[0]

	info = Label(right_frame, text='NOTES', bg='#4d4d4d', fg='white')
	info.grid(row=3, pady=2)
	info2 = Label(right_frame, text='EDT', bg='#4d4d4d', fg='white')
	info2.grid(row=0, pady=2)
	full = date + data
	notes = Label(frame_taches, text=full, bg='white')
	notes.grid()
	var = StringVar()
	var.set('Take a Note')
	entry_taches = Entry(right_frame, textvariable=var)
	entry_taches.grid(row=5, ipadx=80, pady=6)

	VERIF = ("'" + current_user + "'")
	c_horaires.execute("SELECT lundi, lundi0 FROM t_hor WHERE user = " + VERIF)
	Lundi = c_horaires.fetchall()
	c_horaires.execute("SELECT mardi, mardi0 FROM t_hor WHERE user = " + VERIF)
	Mardi = c_horaires.fetchall()
	c_horaires.execute("SELECT mercredi, mercredi0 FROM t_hor WHERE user = " + VERIF)
	Mercredi = c_horaires.fetchall()
	c_horaires.execute("SELECT jeudi, jeudi0 FROM t_hor WHERE user = " + VERIF)
	Jeudi = c_horaires.fetchall()
	c_horaires.execute("SELECT vendredi, vendredi0 FROM t_hor WHERE user = " + VERIF)
	Vendredi = c_horaires.fetchall()
	c_horaires.execute("SELECT samedi, samedi0 FROM t_hor WHERE user = " + VERIF)
	Samedi = c_horaires.fetchall()
	c_horaires.execute("SELECT dimanche, dimanche0 FROM t_hor WHERE user = " + VERIF)
	Dimanche = c_horaires.fetchall()

	lundi = str(Lundi)
	lundi_comma = lundi.replace(",", " /")
	lundi_quotes = lundi_comma.replace("'", "")
	lundi_par1 = lundi_quotes.replace("(", "")
	lundi_par2 = lundi_par1.replace(")", "")
	lundi_ac1 = lundi_par2.replace("[", "")
	lundi_ac2 = lundi_ac1.replace("]", "")
	mardi = str(Mardi)
	mardi_comma = mardi.replace(",", " /")
	mardi_quotes = mardi_comma.replace("'", "")
	mardi_par1 = mardi_quotes.replace("(", "")
	mardi_par2 = mardi_par1.replace(")", "")
	mardi_ac1 = mardi_par2.replace("[", "")
	mardi_ac2 = mardi_ac1.replace("]", "")
	mercredi = str(Mercredi)
	mercredi_comma = mercredi.replace(",", " /")
	mercredi_quotes = mercredi_comma.replace("'", "")
	mercredi_par1 = mercredi_quotes.replace("(", "")
	mercredi_par2 = mercredi_par1.replace(")", "")
	mercredi_ac1 = mercredi_par2.replace("[", "")
	mercredi_ac2 = mercredi_ac1.replace("]", "")
	jeudi = str(Jeudi)
	jeudi_comma = jeudi.replace(",", " /")
	jeudi_quotes = jeudi_comma.replace("'", "")
	jeudi_par1 = jeudi_quotes.replace("(", "")
	jeudi_par2 = jeudi_par1.replace(")", "")
	jeudi_ac1 = jeudi_par2.replace("[", "")
	jeudi_ac2 = jeudi_ac1.replace("]", "")
	vendredi = str(Vendredi)
	vendredi_comma = vendredi.replace(",", " /")
	vendredi_quotes = vendredi_comma.replace("'", "")
	vendredi_par1 = vendredi_quotes.replace("(", "")
	vendredi_par2 = vendredi_par1.replace(")", "")
	vendredi_ac1 = vendredi_par2.replace("[", "")
	vendredi_ac2 = vendredi_ac1.replace("]", "")
	samedi = str(Samedi)
	samedi_comma = samedi.replace(",", " /")
	samedi_quotes = samedi_comma.replace("'", "")
	samedi_par1 = samedi_quotes.replace("(", "")
	samedi_par2 = samedi_par1.replace(")", "")
	samedi_ac1 = samedi_par2.replace("[", "")
	samedi_ac2 = samedi_ac1.replace("]", "")
	dimanche = str(Dimanche)
	dimanche_comma = dimanche.replace(",", " /")
	dimanche_quotes = dimanche_comma.replace("'", "")
	dimanche_par1 = dimanche_quotes.replace("(", "")
	dimanche_par2 = dimanche_par1.replace(")", "")
	dimanche_ac1 = dimanche_par2.replace("[", "")
	dimanche_ac2 = dimanche_ac1.replace("]", "")

	frame_EDT = Frame(right_frame, bg='white')
	frame_EDT.grid(row=1, ipadx=181, ipady=50)
	frame_EDT.grid_propagate(0)
	EDT = Label(frame_EDT, text='Lundi        -->    ' + lundi_ac2 + '\n' + 'Mardi        -->    ' + mardi_ac2 + '\n' + 'Mercredi  -->    ' + mercredi_ac2 + '\n' + 'Jeudi        -->    ' + jeudi_ac2 + '\n' + 'Vendredi  -->    ' + vendredi_ac2 + '\n' + 'Samedi     -->    ' + samedi_ac2 + '\n' + 'Dimanche -->    ' + dimanche_ac2, bg='white')
	EDT.grid()
	space = Label(right_frame, bg='#013D6B')
	space.grid(row=2, ipadx=180)

def communication():
	destroy_window()
	frame_communication.grid()
	#code here :

	def message():
		user = sqlite3.connect('Database/user_database.db')
		cur = user.cursor()
		cur.execute('SELECT * FROM us_er')
		current_user = cur.fetchone()[0]

		ID_Dest = entry_Dest.get()
		IDest = str(ID_Dest)

		db_message = sqlite3.connect('Database/message.db')
		cursor_message = db_message.cursor()
		cursor_message.execute('CREATE TABLE IF NOT EXISTS notes (message TEXT, byy TEXT, too TEXT)')
		cursor_message.execute('INSERT INTO notes VALUES (:message, :byy, :too)',
			{
				'message':entry.get(),
				'byy':current_user,
				'too':IDest
			})
		db_message.commit()
		db_message.close()
		communication()
	
	def remove():
		RM = ("'" + current_user + "'")

		db_message = sqlite3.connect('Database/message.db')
		cursor_message = db_message.cursor()
		cursor_message.execute('DELETE FROM notes WHERE byy =' + RM)
		db_message.commit()
		db_message.close()

		db_message = sqlite3.connect('Database/message.db')
		cursor_message = db_message.cursor()
		cursor_message.execute('DELETE FROM notes WHERE too =' + RM)
		db_message.commit()
		db_message.close()

		planning_db = sqlite3.connect('Database/planning.db')
		c_planning = planning_db.cursor()
		c_planning.execute('DELETE FROM t_plan WHERE user =' + RM)
		planning_db.commit()
		planning_db.close()
		communication()

	db = sqlite3.connect('Database/database.db')
	cursor = db.cursor()
	cursor.execute('SELECT id, last_name, first_name FROM login')
	id_verif = cursor.fetchone()[0]
	names = cursor.fetchall()

	user = sqlite3.connect('Database/user_database.db')
	cur = user.cursor()
	cur.execute('SELECT * FROM us_er')
	current_user = cur.fetchone()[0]

	db_message = sqlite3.connect('Database/message.db')
	cursor_message = db_message.cursor()
	cursor_message.execute('CREATE TABLE IF NOT EXISTS notes (message TEXT, byy TEXT, too TEXT)')
	cursor_message.execute('SELECT byy FROM notes')
	byy_verif = cursor_message.fetchall()
	cursor_message.execute('SELECT too FROM notes')
	too_verif = cursor_message.fetchall()

	lock_byy=''
	for b in byy_verif:
		if current_user in b:
			db_message = sqlite3.connect('Database/message.db')
			cursor_message = db_message.cursor()
			VERIF = ("'" + current_user + "'")
			cursor_message.execute("SELECT * FROM notes WHERE byy = " + VERIF)
			lock_byy = cursor_message.fetchall()

	lock_too=''
	for t in too_verif:
		if current_user in t:
			db_message = sqlite3.connect('Database/message.db')
			cursor_message = db_message.cursor()
			VERIF = ("'" + current_user + "'")
			cursor_message.execute("SELECT * FROM notes WHERE too = " + VERIF)
			lock_too = cursor_message.fetchall()

	full_mess_by=''
	for fb in lock_byy:
		origin = str(fb)
		rm_comma = origin.replace(",", " >>")
		rm_quotes = rm_comma.replace("'", "")
		rm_par1 = rm_quotes.replace("(", "Message : ")
		rm_par2 = rm_par1.replace(")", "")
		full_mess_by += rm_par2 + '\n'

	full_mess_to=''
	for ft in lock_too:
		origin = str(ft)
		rm_comma = origin.replace(",", " >>")
		rm_quotes = rm_comma.replace("'", "")
		rm_par1 = rm_quotes.replace("(", "Message : ")
		rm_par2 = rm_par1.replace(")", "")
		full_mess_to += rm_par2 + '\n'

	frame_users = Frame(frame_communication, bg='#4d4d4d')
	frame_text = Frame(frame_communication, bg='#4d4d4d')
	frame_users.grid(column=0, row=0, sticky=W, padx=15, pady=10)
	frame_text.grid(column=1, row=0, sticky=W, padx=10)
	frame_label_text = Frame(frame_text, bg='white')
	frame_label_text.grid(row=1, sticky=W, ipadx=290, ipady=291)
	frame_label_text.grid_propagate(0)

	Destinataire = StringVar()
	entry_Dest = Entry(frame_text, textvariable=Destinataire, width=10, bg='white')
	entry_Dest.grid(row=0, sticky=W, ipadx=4, padx=248)
	print_Dest = Label(frame_text, text='ID -->')
	print_Dest.grid(row=0, sticky=W, padx=213, pady=2)

	table = ttk.Treeview(frame_users, columns=(1,2,3), show='headings', height=26)
	table.grid(row=1, ipady=25)
	table.heading(1, text='ID')
	table.heading(2, text='Nom')
	table.heading(3, text='Prénom')
	for n in names:
		table.insert('', 'end', values=n)

	news = Label(frame_users, text='Tableau des Utilisateurs', bg='#4d4d4d', fg='white')
	news.grid(row=0, pady=2)
	Buttonn = Button(frame_text, command=message, bg='#4d4d4d', highlightthickness=0, bd=0)
	Buttonn.grid(row=2, ipadx=250, ipady=2, pady=4)
	Text = StringVar()
	Text.set('Say Something')
	entry = Entry(frame_text, textvariable=Text, width=30, bg='white')
	entry.grid(row=2, ipadx=120, ipady=1)
	Buttonn_remove = Button(frame_users, text='Cliquer ici pour supprimer la conversation', command=remove, bg='#4d4d4d', fg='white', highlightthickness=0, bd=0)
	Buttonn_remove.grid(row=2, ipadx=100, pady=4)
	full_mess = full_mess_by + full_mess_to
	query_text = Label(frame_label_text, text=full_mess, bg='white')
	query_text.grid(sticky=W)

def salaire():
	destroy_window()
	frame_salaire.grid()
	frame_horloge=Frame(frame_salaire, bg='snow')
	#code here :

	def tick():
		time1 = time.strftime('%H:%M:%S')
		clock.config(text=time1)
		clock.after(200, tick)

	def temp_login():
		time_salaire = time.strftime('%H:%M:%S')
		datetime_salaire = datetime.strptime(time_salaire,"%H:%M:%S")
		clock2.config(text=datetime_salaire-datetime_login)
		clock2.after(200, temp_login)

	frame_top = Frame(frame_salaire, bg='#013D6B')
	frame_bot = Frame(frame_salaire)
	frame_top1 = Frame(frame_top)
	frame_top2 = Frame(frame_top)
	frame_top3 = Frame(frame_top)
	frame_top.grid(column=0, row=0, pady=50)
	frame_bot.grid(column=0, row=1, sticky=W, ipadx=400, ipady=160, padx=18, pady=15)
	frame_top1.grid(column=0, row=0)
	frame_top2.grid(column=1, row=0)
	frame_top3.grid(column=2, row=0)
	frame_bot.grid_propagate(0)

	banner = Label(frame_top2, text='TIME', fg='white', bg='#4d4d4d')
	banner.grid(column=0, row=0, ipadx=40, ipady=2)
	texte_horloge = Label(frame_top2, text="Heure Actuelle")
	texte_horloge.grid(column=0, row=1)
	clock = Label(frame_top2, font=('times', 20, 'bold'))
	clock.grid(column=0, row=2)
	tick()
	frame_top2.grid(pady=10)

	texte_restant = Label(frame_top2, text="Temp de connexion")
	texte_restant.grid(column=0, row=3)
	clock2 = Label(frame_top2, font=('times', 20, 'bold'))
	clock2.grid(column=0, row=4)
	temp_login()

	cursor_temp.execute('''SELECT jour, heure_login, heure_logout, heure_travail FROM temp WHERE pseudo_temp = ? ''',(pseudo,))
	info_connexion = cursor_temp.fetchall()

	PSEUDO = ("'" + pseudo + "'")
	sal = Label(frame_top1, text='                                         ')
	heure = Label(frame_top3, text='                                       ')
	sal.grid(column=0, row=1, ipady=20)
	heure.grid(column=0, row=1, ipady=20)
	db_sal = sqlite3.connect('Database/salaire.db')
	cursor_sal = db_sal.cursor()
	cursor_sal.execute('CREATE TABLE IF NOT EXISTS sal (pseudo TEXT, sal_month TEXT, sal_hour TEXT)')
	cursor_sal.execute('SELECT sal_month FROM sal WHERE pseudo=' + PSEUDO)
	month = cursor_sal.fetchall()
	months = str(month) + '€'
	rm_comma = months.replace(",", "")
	rm_quotes = rm_comma.replace("'", "")
	rm_par1 = rm_quotes.replace("(", "")
	rm_par2 = rm_par1.replace(")", "")
	rm_ac1 = rm_par2.replace("[", "")
	rm_ac2 = rm_ac1.replace("]", "")
	cursor_sal.execute('SELECT sal_hour FROM sal WHERE pseudo=' + PSEUDO)
	hour = cursor_sal.fetchall()
	hours = str(hour) + '€'
	comma = hours.replace(",", "")
	quotes = comma.replace("'", "")
	par1 = quotes.replace("(", "")
	par2 = par1.replace(")", "")
	ac1 = par2.replace("[", "")
	ac2 = ac1.replace("]", "")
	sal = Label(frame_top1, text=rm_ac2)
	heure = Label(frame_top3, text=ac2)
	sal.grid(column=0, row=1, ipady=20)
	heure.grid(column=0, row=1, ipady=20)

	print_mois = Label(frame_top1, text='Salaire / Mois', fg='white', bg='#4d4d4d')
	print_heures = Label(frame_top3, text='Salaire / Heures', fg='white', bg='#4d4d4d')
	print_mois.grid(column=0, row=0, ipadx=34, ipady=3)
	print_heures.grid(column=0, row=0, ipadx=28, ipady=3)

	table = ttk.Treeview(frame_bot, columns=(1,2,3,4), show='headings', height=26)
	table.grid()
	table.heading(1, text='Jour')
	table.heading(2, text='Heure de connexion')
	table.heading(3, text='Heure de déconnexion')
	table.heading(4, text='Temp de travail')
	for n in info_connexion:
		table.insert('', 'end', values=n)

time_login = time.strftime('%H:%M:%S')
datetime_login = datetime.strptime(time_login, "%H:%M:%S")
jour_login = time.strftime('%d/%m/%y')
db_temp = sqlite3.connect('Database/database_login3.db')
cursor_temp = db_temp.cursor()
cursor_temp.execute('CREATE TABLE IF NOT EXISTS temp (pseudo_temp TEXT, jour TEXT, heure_login TEXT, heure_logout TEXT, heure_travail TEXT)')

user = sqlite3.connect('Database/user_database.db')
cur = user.cursor()
cur.execute('SELECT * FROM us_er')
first_username = cur.fetchone()[1]
cur.execute('SELECT * FROM us_er')
last_username = cur.fetchone()[2]
cur.execute('SELECT * FROM us_er')
pseudo = cur.fetchone()[0]
user.commit()
user.close()

window = tk.Tk()
window.title('BusinessTech')
window.geometry('1280x720')
window.config(background='#013D6B')
window.resizable(width=False, height=False)

identity = ("Nom : " +last_username + "\n Prénom : " + first_username)

frame_accueil = Frame(window, bg='#013D6B')
frame_accueil.grid()
frame_planning = Frame(window, bg='#013D6B')
frame_planning.grid()
frame_communication = Frame(window, bg='#013D6B')
frame_communication.grid()
frame_salaire = Frame(window, bg='#013D6B')
frame_salaire.grid()

menu_sup = tk.PanedWindow(window, background='blue', height=60, width=1280, orient=HORIZONTAL, bd=0)
menu_sup.grid(column=0,row=0, sticky=W)
button_accueil = tk.Button (menu_sup, text="Accueil",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue',  width=15, justify=CENTER, command=accueil) 
menu_sup.add(button_accueil)
button_planning = tk.Button (menu_sup,text="Planning",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER, command=planning)
menu_sup.add(button_planning)
button_com = tk.Button (menu_sup,text="Communication",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER, command=communication) 
menu_sup.add(button_com)
button_salaire = tk.Button (menu_sup, text="Salaire",foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, justify=CENTER, command=salaire) 
menu_sup.add(button_salaire)
button_infos = tk.Menubutton (menu_sup, text=identity,foreground='white', activebackground='cyan' , font=("Arial", 20), background='blue', width=15, anchor='w',)
menu_sup.add(button_infos)

deroulant_infos = Menu(button_infos)
deroulant_infos.add_command(label="déconnexion",background='red', command=logout)
button_infos.configure(menu=deroulant_infos)

icon = tk.PhotoImage(file='Image/bt.gif')
window.iconphoto(True, icon)
window.mainloop()
