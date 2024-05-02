import sqlite3

db=sqlite3.connect("Task7Database.db")
cursor= db.cursor()
sql="SELECT* FROM Planes;"
cursor.execute(sql)
results=cursor.fetchall()
for i in results:
    print(i)
db.close()
