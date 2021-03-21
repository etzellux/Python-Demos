#%% JSON DATA----SPACE HOLDER/USERS
import json
with open("users.json") as users:
    data = json.load(users) #JSON DATASINI ÇEKİP LİSTE OLARAK AKTARDIK
    print(data[0])          #LISTE PEK ÇOK DICT IÇERIYOR
    print("\n\n*****************\n\n")
    print(data[0]["address"]["street"])
    