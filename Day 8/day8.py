##########################.......................if....else.... conditions......###################################################

name = ["ajay", "abi", "bala", "charan", "shankar"]


#basic if condition
if "ajay" in name:
    print("Ajay is present")


##########################################################################################################################################

#if with more than one condition
emp1 = {
    "name": "Manjunath",
    "company": "JFH",
    "role": "DevOps", 
    "team": "Eng"
}

if emp1["company"] == "salesfore" and (emp1["team"] == "CS" or emp1):
    print(emp1["name"]+" is from CS DEPT")


if (emp1["company"] == "dell") or emp1["team"] == "Eng":
    print(emp1["name"]+" is from Engineering DEPT")

##########################################################################################################################################

#writing else condition

a = input("Enter value for a: ") #input() is used to get input from the user from the console
b = input("Enter value for b: ")

if b>a:
    print("b is greater")
else:
    print("a is greater")



############################################################################################################################

#nested if

a = 10
b = 30
c = 20


if b>a:
    if c>b:
        print("c is greater")
    else:
        print("b is greater")
else:
    if c>a:
        print("c is greater")
    else:
        print("a is greater")
    


############################################################################################################################

#if else ladder

emp1 = {
    "name": "Manjunath",
    "company": "JFH",
    "role": "candidate", 
    "team": "Eng"
}


if emp1["role"] == "LEAD":
    print("All access given")
elif emp1["role"] == "DevOps":
    print("Give DevOPS access")
elif emp1["role"] == "Dev":
    print("Give Dev access")
else:
    print("Give basic access")

#############################################################################################################

#using pass keyword

emp1 = {
    "name": "Manjunath",
    "company": "DELL",
    "role": "candidate", 
    "team": "Eng",
    "verified": True
}


if emp1["verified"] is True:
    pass #wont do anything, its like a clear to go FLAG
else:
    print("verification complete")
    emp1["verified"] = True

########################################################################################

a=100
b=20
#short hand if
if b>a: print("b is bigger")






#regular if else
if b>a:
    print("b is greater")
else:
    print("a is greater")

#short hand if..else
print("b is bigger") if b>a else print("a is greater")  #(if the condition is true, do this)if (condition) else (do this)


#do this operation IF (condition is true) else (do this)