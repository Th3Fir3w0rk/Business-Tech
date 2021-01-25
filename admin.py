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

def new_user():
	os.system('python new_user.py')

def remove_user():
	os.system('python remove_user.py')

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

	def update():
		USER = ("'" + entry_User.get() + "'")
		horaires = sqlite3.connect('Database/horaires.db')
		c_horaires = horaires.cursor()
		c_horaires.execute('CREATE TABLE IF NOT EXISTS t_hor (user TEXT, lundi TEXT, mardi TEXT, mercredi TEXT, jeudi TEXT, vendredi TEXT, samedi TEXT, dimanche TEXT, lundi0 TEXT, mardi0 TEXT, mercredi0 TEXT, jeudi0 TEXT, vendredi0 TEXT, samedi0 TEXT, dimanche0 TEXT)')
		c_horaires.execute('DELETE FROM t_hor WHERE user = ' + USER)
		c_horaires.execute('INSERT INTO t_hor VALUES (:user, :lundi, :mardi, :mercredi, :jeudi, :vendredi, :samedi, :dimanche, :lundi0, :mardi0, :mercredi0, :jeudi0, :vendredi0, :samedi0, :dimanche0)',
		{
			'user':entry_User.get(),
			'lundi':entry_Lundi.get(),
			'mardi':entry_Mardi.get(),
			'mercredi':entry_Mercredi.get(),
			'jeudi':entry_Jeudi.get(),
			'vendredi':entry_Vendredi.get(),
			'samedi':entry_Samedi.get(),
			'dimanche':entry_Dimanche.get(),
			'lundi0':entry_Lundi0.get(),
			'mardi0':entry_Mardi0.get(),
			'mercredi0':entry_Mercredi0.get(),
			'jeudi0':entry_Jeudi0.get(),
			'vendredi0':entry_Vendredi0.get(),
			'samedi0':entry_Samedi0.get(),
			'dimanche0':entry_Dimanche0.get()
		})
		horaires.commit()
		horaires.close()
		planning()

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
	frame_taches.grid(row=4, ipadx=180, ipady=180)
	frame_taches.grid_propagate(0)

	user = sqlite3.connect('Database/user_database.db')
	cur = user.cursor()
	cur.execute('SELECT * FROM us_er')
	current_user = cur.fetchone()[0]

	calendar = Calendar(left_frame, selectmode='day')
	calendar.grid(ipadx=300, ipady=240)
	bt_get_date = Button(right_frame, command=is_pressed, bg='#4d4d4d', highlightthickness=0, bd=0)
	bt_get_date.grid(row=5, ipadx=165)

	planning_db = sqlite3.connect('Database/planning.db')
	c_planning = planning_db.cursor()
	TT = ("'" + current_user + "'")
	c_planning.execute("SELECT date, note FROM t_plan WHERE user =" + TT)
	date_db = c_planning.fetchall()
	
	date=''
	for d in date_db:
		origin = str(d)
		rm_comma = origin.replace(",", " : ")
		rm_quotes = rm_comma.replace("'", "")
		rm_par1 = rm_quotes.replace("(", "")
		rm_par2 = rm_par1.replace(")", "")
		date += rm_par2 + '\n'

	horaires = sqlite3.connect('Database/horaires.db')
	c_horaires = horaires.cursor()
	c_horaires.execute('SELECT * FROM t_hor')
	act_user = c_horaires.fetchone()[0]

	info = Label(right_frame, text='NOTES', bg='#4d4d4d', fg='white')
	info.grid(row=3, pady=2)
	info2 = Label(right_frame, text='EDT', bg='#4d4d4d', fg='white')
	info2.grid(row=0, pady=2)
	taches = Label(frame_taches, text=date, bg='white')
	taches.grid()
	var = StringVar()
	var.set('Note For All Users')
	entry_taches = Entry(right_frame, textvariable=var)
	entry_taches.grid(row=5, ipadx=80, pady=6)

	frame_EDT = Frame(right_frame)
	frame_EDT.grid(row=1, ipadx=181, ipady=90)
	frame_EDT.grid_propagate(0)
	space = Label(right_frame, bg='#013D6B')
	space.grid(row=2, ipadx=180)

	frame_ID = Frame(frame_EDT)
	frame_days = Frame(frame_EDT)
	frame_update = Frame(frame_EDT)
	frame_ID.grid(column=0, row=0)
	frame_days.grid(column=0, row=1)
	frame_update.grid(column=0, row=2)

	label_User = Label(frame_ID, text='ID User')
	label_User.grid(column=0, row=0)
	label_Lundi = Label(frame_days, text='Lundi        -->')
	label_Lundi.grid(column=0, row=0)
	label_Mardi = Label(frame_days, text='Mardi        -->')
	label_Mardi.grid(column=0, row=1)
	label_Mercredi = Label(frame_days, text='Mercredi  -->')
	label_Mercredi.grid(column=0, row=2)
	label_Jeudi = Label(frame_days, text='Jeudi        -->')
	label_Jeudi.grid(column=0, row=3)
	label_Vendredi = Label(frame_days, text='Vendredi  -->')
	label_Vendredi.grid(column=0, row=4)
	label_Samedi = Label(frame_days, text='Samedi     -->')
	label_Samedi.grid(column=0, row=5)
	label_Dimanche = Label(frame_days, text='Dimanche -->')
	label_Dimanche.grid(column=0, row=6)

	ll = Label(frame_days, text='/')
	ll.grid(column=2, row=0)
	lma = Label(frame_days, text='/')
	lma.grid(column=2, row=1)
	lme = Label(frame_days, text='/')
	lme.grid(column=2, row=2)
	lj = Label(frame_days, text='/')
	lj.grid(column=2, row=3)
	lv = Label(frame_days, text='/')
	lv.grid(column=2, row=4)
	ls = Label(frame_days, text='/')
	ls.grid(column=2, row=5)
	ld = Label(frame_days, text='/')
	ld.grid(column=2, row=6)

	User = StringVar()
	entry_User = Entry(frame_ID, textvariable=User)
	entry_User.grid(column=1, row=0)
	Lundi = StringVar()
	Lundi.set('.................')
	entry_Lundi = Entry(frame_days, textvariable=Lundi)
	entry_Lundi.grid(column=1, row=0)
	Mardi = StringVar()
	Mardi.set('................')
	entry_Mardi = Entry(frame_days, textvariable=Mardi)
	entry_Mardi.grid(column=1, row=1)
	Mercredi = StringVar()
	Mercredi.set('................')
	entry_Mercredi = Entry(frame_days, textvariable=Mercredi)
	entry_Mercredi.grid(column=1, row=2)
	Jeudi = StringVar()
	Jeudi.set('................')
	entry_Jeudi = Entry(frame_days, textvariable=Jeudi)
	entry_Jeudi.grid(column=1, row=3)
	Vendredi = StringVar()
	Vendredi.set('................')
	entry_Vendredi = Entry(frame_days, textvariable=Vendredi)
	entry_Vendredi.grid(column=1, row=4)
	Samedi = StringVar()
	Samedi.set('................')
	entry_Samedi = Entry(frame_days, textvariable=Samedi)
	entry_Samedi.grid(column=1, row=5)
	Dimanche = StringVar()
	Dimanche.set('................')
	entry_Dimanche = Entry(frame_days, textvariable=Dimanche)
	entry_Dimanche.grid(column=1, row=6)
	Lundi0 = StringVar()
	Lundi0.set('................')
	entry_Lundi0 = Entry(frame_days, textvariable=Lundi0)
	entry_Lundi0.grid(column=3, row=0)
	Mardi0 = StringVar()
	Mardi0.set('................')
	entry_Mardi0 = Entry(frame_days, textvariable=Mardi0)
	entry_Mardi0.grid(column=3, row=1)
	Mercredi0 = StringVar()
	Mercredi0.set('................')
	entry_Mercredi0 = Entry(frame_days, textvariable=Mercredi0)
	entry_Mercredi0.grid(column=3, row=2)
	Jeudi0 = StringVar()
	Jeudi0.set('................')
	entry_Jeudi0 = Entry(frame_days, textvariable=Jeudi0)
	entry_Jeudi0.grid(column=3, row=3)
	Vendredi0 = StringVar()
	Vendredi0.set('................')
	entry_Vendredi0 = Entry(frame_days, textvariable=Vendredi0)
	entry_Vendredi0.grid(column=3, row=4)
	Samedi0 = StringVar()
	Samedi0.set('................')
	entry_Samedi0 = Entry(frame_days, textvariable=Samedi0)
	entry_Samedi0.grid(column=3, row=5)
	Dimanche0 = StringVar()
	Dimanche0.set('................')
	entry_Dimanche0 = Entry(frame_days, textvariable=Dimanche0)
	entry_Dimanche0.grid(column=3, row=6)

	update = Button(frame_update, text='UPDATE', command=update)
	update.grid(column=1, row=8, ipadx=40, pady=2)

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
		db_message = sqlite3.connect('Database/message.db')
		cursor_message = db_message.cursor()
		cursor_message.execute('DELETE FROM notes')
		db_message.commit()
		db_message.close()

		planning_db = sqlite3.connect('Database/planning.db')
		c_planning = planning_db.cursor()
		c_planning.execute('DELETE FROM t_plan')
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
	Buttonn_remove = Button(frame_users, text='Cliquer ici pour supprimer toutes les conversations', command=remove, bg='#4d4d4d', fg='white', highlightthickness=0, bd=0)
	Buttonn_remove.grid(row=2, ipadx=100, pady=4)
	full_mess = full_mess_by + full_mess_to
	query_text = Label(frame_label_text, text=full_mess, bg='white')
	query_text.grid(sticky=W)

def salaire():
	destroy_window()
	frame_salaire.grid()
	frame_horloge=Frame(frame_salaire, bg='snow')
	#code here :

	def view_user():
		PSEUDO = ("'" + ID_User.get() + "'")
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

		frame_bot = Frame(frame_salaire)
		frame_bot.grid(column=0, row=1, sticky=W, ipadx=400, ipady=160, padx=18, pady=15)
		frame_bot.grid_propagate(0)
		for u in frame_bot.winfo_children():
			frame_bot.grid_forget()
		cursor_temp = db_temp.cursor()
		cursor_temp.execute('CREATE TABLE IF NOT EXISTS temp (pseudo_temp TEXT, jour TEXT, heure_login TEXT, heure_logout TEXT, heure_travail TEXT)')
		cursor_temp.execute('SELECT jour, heure_login, heure_logout, heure_travail FROM temp WHERE pseudo_temp =' + PSEUDO)
		info_connexion = cursor_temp.fetchall()
		table = ttk.Treeview(frame_bot, columns=(1,2,3,4), show='headings', height=26)
		table.grid()
		table.heading(1, text='Jour')
		table.heading(2, text='Heure de connexion')
		table.heading(3, text='Heure de déconnexion')
		table.heading(4, text='Temp de travail')
		for n in info_connexion:
			table.insert('', 'end', values=n)


	def update_user():
		PSEUDO = ("'" + ID_User.get() + "'")
		db_sal = sqlite3.connect('Database/salaire.db')
		cursor_sal = db_sal.cursor()
		cursor_sal.execute('CREATE TABLE IF NOT EXISTS sal (pseudo TEXT, sal_month TEXT, sal_hour TEXT)')
		cursor_sal.execute('DELETE FROM sal WHERE pseudo =' + PSEUDO)
		cursor_sal.execute('INSERT INTO sal VALUES (:pseudo, :sal_month, :sal_hour)',
		{
			'pseudo':ID_User.get(),
			'sal_month':entry_salaire.get(),
			'sal_hour':entry_heure.get()
		})
		db_sal.commit()
		db_sal.close()
		salaire()

	frame_top = Frame(frame_salaire, bg='#013B6D', pady=8)
	frame_bot = Frame(frame_salaire)
	frame_top1 = Frame(frame_top)
	frame_top2 = Frame(frame_top)
	frame_top3 = Frame(frame_top)
	frame_choice = Frame(frame_top2)
	frame_top.grid(column=0, row=0, pady=50)
	frame_bot.grid(column=0, row=1, sticky=W, ipadx=400, ipady=160, padx=18, pady=15)
	frame_top1.grid(column=0, row=0)
	frame_top2.grid(column=1, row=0)
	frame_top3.grid(column=2, row=0)
	frame_choice.grid(column=0, row=1)
	frame_bot.grid_propagate(0)

	label_color = Label(frame_top2, text='SELECTION', fg='white', bg='#4d4d4d')
	label_color.grid(column=0, row=0, ipadx=60, ipady=2)

	lab = Label(frame_choice, text='ID User')
	lab.grid(column=0, row=0, pady=25)
	ID_User = Entry(frame_choice)
	ID_User.grid(column=1, row=0)
	button_ID = Button(frame_top2, text='View User', command=view_user)
	button_ID.grid(column=0, row=2, ipadx=53)
	button_up = Button(frame_top2, text='Update User', command=update_user)
	button_up.grid(column=0, row=3, ipadx=47)

	sal = Label(frame_top1, text='')
	heure = Label(frame_top3, text='')
	sal.grid(column=0, row=1, ipady=20)
	heure.grid(column=0, row=1, ipady=20)

	esal = StringVar()
	emon = StringVar()
	esal.set('Monthly Amount')
	emon.set('Hourly Amount')
	print_salaire = Label(frame_top1, text='Salaire / Mois', fg='white', bg='#4d4d4d')
	print_heure = Label(frame_top3, text='Salaire / Heures', fg='white', bg='#4d4d4d')
	entry_salaire = Entry(frame_top1, textvariable=esal)
	entry_heure = Entry(frame_top3, textvariable=emon)
	print_salaire.grid(column=0, row=0, ipadx=34, ipady=3)
	print_heure.grid(column=0, row=0, ipadx=28, ipady=3)
	entry_salaire.grid(column=0, row=2)
	entry_heure.grid(column=0, row=2)

	table = ttk.Treeview(frame_bot, columns=(1,2,3,4), show='headings', height=26)
	table.grid()
	table.heading(1, text='Jour')
	table.heading(2, text='Heure de connexion')
	table.heading(3, text='Heure de déconnexion')
	table.heading(4, text='Temp de travail')

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
deroulant_infos.add_command(label="New User", command=new_user)
deroulant_infos.add_command(label="Remove User", command=remove_user)
deroulant_infos.add_command(label="déconnexion",background='red', command=logout)
button_infos.configure(menu=deroulant_infos)

icon = tk.PhotoImage(file='Image/bt.gif')
window.iconphoto(True, icon)
window.mainloop()