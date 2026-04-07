import sqlite3


conn=sqlite3.connect("Luffy.db")

cursor = conn.cursor()


query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'empire earth', 'C:\\Users\\IT Kalyani\\AppData\\Local\\Programs\\Empire Earth\\Empire Earth\\Empire Earth.exe')"
#cursor.execute(query)
#conn.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO web_command VALUES (null,'iemcrp', 'https://www.iemcrp.com/')"
#cursor.execute(query)
#conn.commit()





