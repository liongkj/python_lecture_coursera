import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'
fh = open(fname).readlines()

for line in fh:
    emails = re.findall(r'^From .+@(.+?)\s', line)
    if len(emails) > 0:
        email = emails[0]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('''INSERT INTO Counts (org, count)
                    VALUES (?, 1)''', (email,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                        (email,))
        conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
