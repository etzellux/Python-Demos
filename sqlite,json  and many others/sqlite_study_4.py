import sqlite3 

connection = sqlite3.connect("chinook.db")  #connection ismiyle dbye erişim sağlayacak örnekleme

cursor = connection.execute("""select FirstName,LastName from customers
                            where FirstName like '%y%'""")
#LIKE KEYWORDU BURADA ISMININ ICINDE Y GEÇEN GIRDILERI GETIRDI

for row in cursor:
    print("firstname:" + row[0])
    print("lastname:" + row[1])
    print("*********************")

connection.close()

