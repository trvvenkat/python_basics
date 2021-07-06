print("this is my 1st py program")

###########################################################################################

#indentation example
if 20>10: #hey here i am comparing 2 numbers using greater than symbol
    print("20 is greater than 10")
if 30>20:
    #sdlkfndsklj
    print ("next layer")


##########################################################################


#variables and data types
value_1 = 10
value2 = "20"
name = 'manjunath'

print(value_1)
print(name)

if int(value2)>value_1:
    print("this works too")



x = str(10)
y = int(10)
z = float(10)

print(type(x))
print(type(y))
print(type(z))

################################################################################################



#python lists
numbers = [1, 2, 3]

a = 10
b = 20
c = 30

#assigning multiple values in single line
a, b, c = 10, 20, 30

d, e, f = numbers


print(a)
print(b)
print(c)

print(d)
print(e)
print(f)


###########################################################################################


name = "manjunath"
id = 10
id_str = str(id) #converting a int type to str and storing in a separate variable for later use

print("my name is "+name) #string concatenation
print("my id is "+str(id)) #string concat by using different datatypes (converting into str)
print("my id is "+id_str)
print(type(id))



a = 10
b = 20

print(a+b)

######################################################################################

#global and local variables

name = "venkat" #global variable

def print_my_name():
    name = "manjunath" #local variable
    print("my name is "+name)


print(name)
print_my_name()
print(name)


###############################################################################################


#basic string operations


#assigning a multi-line string value to a variable
a = '''my name is manjunath.
i work at JFH
i am a DevOPS Eng
Venkat is very ok'''
print(a)


texts = "apple"
print(texts[3]) #position

for text in texts: #basic for loop
    print(text)

print(len(a)) #length of a variable - len()


#example for "in" keyword
if "DevOPS" in a:
    print("it is there")

if "bad" not in a:
    print("this is good sentence")


###############################################################################################