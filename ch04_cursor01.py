import sqlite3

conn = sqlite3.connect('test')
cursor = conn.cursor()

sqlstr = 'CREATE TABLE IF NOT EXISTS "phone"("num" INTEGER PRIMARY KEY NOT NULL , "tel" TEXT)'
cursor.execute(sqlstr)

sqlstr = 'insert into phone values(2, "02-1234568")'
cursor.execute(sqlstr)

conn.commit()
conn.close()