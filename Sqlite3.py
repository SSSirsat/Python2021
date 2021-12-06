#sqlite3
import sqlite3
con = sqlite3.connect("mydatabase.db")
cursorobj = con.cursor()
sql_text = "Create Table Students(ID Integer PRIMARY KEY, Name Text, Branch Text)"


sql_text = "Select * from Students"
cursorobj.execute(sql_text)
rows = cursorobj.fetchall()
for row in rows:
    print("Info: ", row)