import sqlite3

connection = sqlite3.connect("chinook.db")
connection.execute("update customers set city = 'İstanbul' where firstName='Atilla'")
data = connection.execute("select firstName,lastName,city from customers")
for row in data:
    print("firstName:" + row[0])
    print("lastName:" + row[1])
    print("city:" + row[2])
    print("************")
connection.close()