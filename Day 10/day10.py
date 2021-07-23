###############################..................Functions......................###################################

# name = "venkat"
# print(name)
# name = "Manjunath"
# print(name)
# name = "charan"
# print(name)


#def - function definition
def print_name():
    #functionalities
    name = input("enter yout name: ")
    print(name)


print_name()#function call  -----  we can call the function any number of time to use the functionality written in
print_name()

###################################################################################################################


#functions with parameters
def print_name(name):
    print(name)


print_name("manjunath")#argument being passed for a parameterized funtion
print_name("Venkat")




#default arguments
def print_name(name="CHARAN"):
    print(name)


print_name("manjunath")
print_name()# here even if we dont pass any value as an argument for the parameterized function, it will not throw an error, because it has a default value

##############################################################################################################################

def print_name(name, age, company): #any number of parameters can be defined. as per we need to pass the arguments!
    print(name+" is of age "+str(age)+" is working at "+company)


print_name("manjunath", 25, "JFH")
print_name("Venkat", 25, "C4ETech")

##################################################################################################################################

#keyword arguments

def print_name(name, age, company):
    print(name+" is of age "+str(age)+" is working at "+company)


print_name(name="Manjunath", company="JFH", age=25) 
#passing keyword argument means, we can misplace the position of arguments and still avoid the error, 
#but we need to give the EXACT VALRIABLE NAME WHICH IS IN THE PARAMETER OF THE FUNCTION AS A KEYWORD WHEN CALLING IT

print_name(company="TOY", name="Venkat", age=3000)

###################################################################################################################################

#arbitary keyword arguments (**kwargs)
def print_name(**arg):
    print(type(arg))
    print(arg)
    print(arg["name"]+" is of age "+str(arg["age"])+" is working at "+arg["company"]+" located in "+arg["location"])


print_name(name="Manjunath", company="JFH", age=25, location="Banglore", role="DevOPS", lead="Charan", boss="neha", enemy="venkat")

##########################################################################################################################

def print_name(name):
    print(name)

name_l = ["manjunath", "venkat"]
print_name(name_l)#we can use/pass values of any type of data in python functions (for demo we have used lists)

#####################################################################################################################

#retun statement in python

def compare(x,y):
    if x>y:
        return x
    else:
        return str(y)+" is greater than "+str(x)


a=100
b=20
result = compare(a,b)
print(result)


#example of how other programming languages handle return 
# int func_name()
# {
#     a=10
#     b=20
#     c=a+b
#     return c
# }