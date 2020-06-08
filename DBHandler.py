import sqlite3 as sql

def retrieveUsers():
	con = sql.connect("Diabetic Retinopathy.db")
	cur = con.cursor()
	cur.execute("SELECT userid, password FROM Users")
	users = cur.fetchall()
	con.close()
	return users

def retrieveReport(name):
	con = sql.connect("Diabetic Retinopathy.db")
	cur = con.cursor()
	cur.execute("SELECT DR_Test, DR_Severity FROM DR_Patients_Details where Full_Name= '%s'" %name)
	details = cur.fetchall()
	con.close()
	return details
