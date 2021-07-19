########....................................DICTIONARY OPERATIONS..........................######################

data = {
    "name": "manjunath",
    "company": "JFH",
    "desig": "DEVOPS ENG",
    "year": 2021, 
    "education": ["SSLC", "HSC", "Engineering"],
    "working": True,
    "location": None
}



data['home'] = "Banglore" #add new {"key": "value"} to an existing dictionary

print(data)
data['desig'] = "BACKEND ENG" #updating the value (method 1)
print(data)

data.update({"year": "2020, 2021"}) #updating the value by using .update()
print(data)

######################################################################################################################
#removing items from the dictionary


data.pop("education") #to remove the given key from the dictionary
print(data)

data.popitem()# to remove the last {"key": "value"} from the dictionary
print(data)

del data["name"]#only if we specify the "key" it will delete the {"key": "value"}, else it will delete the entire variable !!!---BEWARE---!!!
print(data)

del data 
data = {
    "name": "manjunath",
    "company": "JFH",
    "desig": "DEVOPS ENG",
    "year": 2021, 
    "education": ["SSLC", "HSC", "Engineering"],
    "working": True,
    "location": None
}
print(data)

#########################################################################################################################
#accessing values in a dictionary

for item in data: #each time the key will get assigned to the item
    print(item) #this will print the keys of the given dictionary
    print(data[item]) #this will print the values of the given dictionary

print("..........................................................................................")
for item in data.values(): #to get "values" from the dictionary instead of keys
    print(item)


print("..........................................................................................")

for x, y in data.items(): #to get both "key" and "value"
    print(x, y)


############################################################################################################################

#ways to copy a dictionary

x = data #method 1

y = x.copy() #method 2

z = dict(data) #method 3

############################################################################################################################

#dictionary inside a dictionary
manjuanth = {
    "name": "manjunath",
    "company": "JFH",
    "desig": "DEVOPS ENG",
    "year": 2021, 
    "education": ["SSLC", "HSC", "Engineering"],
    "working": True,
    "location": None
}


dict1 = {
    "JFH_183": {
        "name": "venkat",
        "desig": "Junior Software Dev"
    }, 
    "JFH_150": manjuanth
}

print(dict1)

list1 = [1,2,3,4]
list2 = ["a", "b", "c"]
list_final = [list1, list2, manjuanth]