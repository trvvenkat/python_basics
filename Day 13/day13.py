############################.................Classes and Objects..............##################################
#understanding of classes 


#python is a object oriented language
#almost everything you use in python is based on objects and functions


# def add_name()
# def add_depat()
# . 
# . 
# .


# COMPANY

# emp_1_name = "manjunath"
# emp_1_dept = "server, tech, devops"
# emp_1_id = 12


# emp_1 = name, dept, history


########################################################################################################################

#class & object syntax and creation
class Employer:
    name = "manjunath"
    dept = "devops"
    
    def get_name(self):
        return self.name


#class Classname (class name should start with caps always)

emp1 = Employer() #object creation
#print(emp1.dept)
#print(emp1.name)
print(emp1.get_name())

emp2 = Employer()

############################################################################################################################

#constructor and how to use it

class Employer:
    #__init__() is called as a constructor method - this will automatically executed when we create an object - we can also have parameters for this
    def __init__(self, name, dept):
        self.location = "banglore"
        self.name = name
        self.dept = dept

    def get_name(self):
        return self.name
    
emp1 = Employer("manjunath", "devops")
emp2 = Employer("Venkat", "backend DEV")

print(emp1.dept)
print(emp1.location)
print(emp2.dept)
print(emp1.get_name())

#self parameter is like a keyword - when we use it with an variable, 
# it will create an instance of it so that we can use it all over inside class - 
# also outside the class by using object 
# when we use self keyword for a variable it is called as an instance variable



#methods and functions are same - functions inside a class are called as methods - 
