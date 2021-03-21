import sqlite3 

connection = sqlite3.connect("chinook.db")  #connection ismiyle dbye erişim sağlayacak örnekleme
# SIRALAMALAR= ORDER BY ------- (DEFAULT) ASC(ASCENDING) / DESCENDING 
cursor = connection.execute("""select FirstName,LastName from customers
                            where city = 'Prague' or city='Berlin'
                            order by FirstName,LastName desc""")

for row in cursor:
    print("firstname:" + row[0])
    print("lastname:" + row[1])
    print("*********************")

connection.close()
