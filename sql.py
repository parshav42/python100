import sqlite3

conn = sqlite3.connect('empaloy.db')

coursor = conn.cursor()
# #
# # coursor.execute('''CREATE TABLE employ  (id INTEGER PRIMARY KEY , name TEXT ,salary REAL, department TEXT )''')
# #
# # conn.commit()
# #
# # conn.close()
#
# coursor.execute('''SELECT * FROM employ''')
#
# fet = coursor.fetchall()
#
# print(fet)
#
# conn.close()

coursor.execute('''INSERT INTO employ (name,salary,department) VALUES(? , ? , ?)''',('omkar',21098,'oracal'),('sudhir',4534534,'it'))

conn.commit()

conn.close()