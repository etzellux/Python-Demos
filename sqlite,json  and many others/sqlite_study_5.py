import sqlite3

connection = sqlite3.connect("chinook.db")
connection.execute("""insert into customers (firstName,lastName,city,email) 
                                      values('Atilla','Semerci','İstanbul','tfslayer')""")

data = connection.execute("select firstName,lastName,email from customers order by firstName")
for row in data:
    print("firstName:" + row[0])
    print("lastName:" + row[1])
    print("Email:" + row[2])
    print("*******************")
connection.commit()
connection.close()