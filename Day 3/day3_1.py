######################                                                   BOOLEAN                                     ###################

########################################################################################
a = 10
b = 20

if not (b>a): #boolean
    print("b is the bigger one")
else:
    print("something else")




print (b>a) #comparison of variables will return boolean
print(10 == 10.0)



name = "manjunath"
print("m" in name) #boolean return values by using strings

########################################################################################

z = "apple"
x = 0 #0's will be considered as Flase and 1's will be considered as True


print(bool(x)) #to return a boolean value for a given variable
print(bool(z))
 #NOTE: Max all the values are True if it is not None(null)

############################################################################################

def get_access(): #using boolean in functions
    return True, "manjunath"


access, name = get_access()

if access:
    print("got the access "+name)
else:
    print("access denied")


################################################################################################

num = "200"
print(isinstance(num, str)) #check the variable is of given datatype

##############################################################################################