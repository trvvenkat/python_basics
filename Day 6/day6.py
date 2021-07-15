########################........................Python Dictionaries.............................##############################
#dictionaries are similar to JSON

data = {
    "name": "manjunath",
    "company": "JFH",
    "desig": "DEVOPS ENG",
    "year": 2021, 
    "education": ["SSLC", "HSC", "Engineering"],
    "working": True
}

#syntax:
#variable = {"key":"value", "KEY": "VALUE", ...n}

print(data["working"]) #if you give key, it will return the value for it

print(len(data))

###################################################################################################################################

name = data["name"]
print(name)

company = data.get("company")
print(company)




data_keys = data.keys() #this will store all the keys of a dictionary to a variable and it is auto updated
print(data_keys)
data["location"] = "Bangalore"
print(data)
print(data_keys)





data_values = data.values() #this will store all the values of a dictionary to a variable and it is auto updated
print(data_values)
print(type(data_values))
data["home_location"] = "Chennai"
print(data_values)




data_items = data.items() #this will store all the keys and values of a dictionary to a variable as a tuple sets and also auto updated
print(data_items)


if "location" in data and data["location"] is not None: #in keyword will check wether the key is present or not
    backend_location = data["location"]
    print(backend_location)
else:
    print("this doesnt have location info")
