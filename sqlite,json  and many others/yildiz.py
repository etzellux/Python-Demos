rownumber = int(input("Satır sayısı giriniz:"))

for i in range(1,rownumber*2,2):
    print((rownumber-i//2)*" " + i*"*")
    


