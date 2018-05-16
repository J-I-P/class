import sqlite3

conn = sqlite3.connect('test')

cursor = conn.execute('select * from phone where num=2')
rows = cursor.fetchone()
print(rows)

if not rows==None:
    print("{}\t{}".format(rows[0],rows[1]))