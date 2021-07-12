###############.......................................Python Lists...........................############################


a_list = ["apple", "orange"]
b_list = [1, 2, 3, 4, 5]
c_list = [True, True, False, True]

d_list = ["Manjunath", 25, True, "Bangalore"] #lists in python supports mixing of multiple datatypes also

print(type(a_list))
print(b_list)
print(c_list)
print(d_list)


#############################################################################################################

fruit1 = "apple"
fruit2 = "banana"
veg1 = "carrot"

grocery = list((fruit1, fruit2, veg1)) #by using list() we can make python create our own list by giving in values as a parameter

print(grocery)

#lists - [1, 2, 3, n]
#sets - { value1, value2, value_n }
#tuples - ( 1, 2, n   )
#dictionaries - { Key: value }

####################################################################################################################

#position and index in list

users = ["manunath", "shankar", "venkat", "charan", "gokul", "pooja", "suchitra", "Kajal", "thulasi"] #list index starts with 0 and position starts at 1
print(users[1])
print(users[-2])

print(users[1:3]) #list[index:position]     will give the list which starts at the given index till the position we give
print(users[:2])

print(users[2:5])


team_tech = ["manunath", "shankar", "venkat", "charan", "gokul", "pooja", "suchitra", "Kajal", "thulasi"]

if "gokul" in team_tech: #checking for values in a list using "in" keyword
    print("he is there")
else:
    print("he is not there")


######################################################################################################################
#updating the values in a list

team_tech = ["manunath", "shankar", "venkat", "charan", "gokul", "pooja", "suchitra", "Kajal", "thulasi"]

print(team_tech)

team_tech[2] = 'Venkatesh' #changing/updating the value of a list using list index
print(team_tech)

team_tech[1:4] = [1, 2, 3] #changing/updating values of a list by giving a range 
print(team_tech)


############################################################################################################################

#adding new values to the list

num_list = ["apple", "orrange", "banana"]
num_list.insert(20, "pineapple") #list.insert(index, "value")
print(num_list)
print(num_list[3])

num_list.append("grape") #list.append(value) will add the given value at the last
print(num_list)

fru = ["apple", "orrange", "banana"]
veg = ["carrot", "beans"]
fru.extend(veg) #too add values from another list to extend the current one we can use ==> list_1.extend(list_2)
print(fru)

########################################################################################################################

#removing / deleting values from the list.......... deleting the entire list

team_tech = ["manunath", "shankar", "venkat", "charan", "gokul", "pooja", "suchitra", "Kajal", "thulasi"]

team_tech.remove("venkat") #removing or deleting a specific value from the list
print(team_tech)

team_tech.pop(-1)#removing or deleting a value by mentioning a specific index
print(team_tech)

list_sample = [1, 2, 3, 4, 5, 6]
list_sample.pop() #if we dont specify any index for pop(), it will pop out the last element in the list
print(list_sample)


del list_sample #del list_name will delete the entire list variable
#print(list_sample)   .....commenting this our because, if we run it, it will throw in an error saying "list_sample not defined". 


team_tech.clear()#list.clear() will clear or delete all the values from the list and will make it as a empty one
print(team_tech)

#####################################################################################################