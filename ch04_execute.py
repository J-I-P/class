import sqlite3

conn = sqlite3.connect('test')
num = 5
tel = "02-76543213"
sqlstr = "insert into phone values({},'{}')".format(num, tel)
conn.execute(sqlstr)

sqlstr = "update phone set tel='{}' where num={}".format("049-2988000", 1)
conn.execute(sqlstr)

sqlstr = "delete from phone where num=1"
conn.execute(sqlstr)

#sqlstr = "DROP TABLE phone"
#conn.execute(sqlstr)

conn.commit()