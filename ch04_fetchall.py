import sqlite3

conn = sqlite3.connect('test')

cursor = conn.execute('select * from phone')
rows = cursor.fetchall()
print(rows)

for row in rows:
    print("{}\t{}".format(row[0],row[1]))