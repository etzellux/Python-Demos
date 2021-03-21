
#%% JSON FORMATINDAN DICTIONARY'E
import json 
data = '{"username":"abs123","id_number":"12345"}'
x = json.loads(data)
print(x)
#%% DICTIONARYDEN JSON FORMATINA
dict1 = {"firstName":"Atilla","contactnumber":"3343223"}
dict1_json = json.dumps(dict1)
print(dict1_json)