import sqlite3 

connection = sqlite3.connect("chinook.db")  #connection ismiyle dbye erişim sağlayacak örnekleme
# SIRALAMALAR= ORDER BY ------- (DEFAULT) ASC(ASCENDING) / DESCENDING 
#cursor = connection.execute("""select FirstName,LastName from customers
#                            where city = 'Prague' or city='Berlin'
#                            order by FirstName,LastName desc""")
cursor = connection.execute("""select city,count(*) from customers group by city 
                            having count(*) > 1  
                            order by count(*) desc""")
                        #HAVING BELIRLI IFADELERI ALIR, ORDER SORTLAR,GROUP GRUPLAR

for row in cursor:
    print("city:" + row[0])
    print("count:" + str(row[1]))
    print("*********************")

connection.close()