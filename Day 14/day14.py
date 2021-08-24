#########################............. Object understanding...............############################

class Employer:
    def __init__(self, name=None, dept=None):
        self.location = "banglore"
        self.name = name
        self.dept = dept

    def get_name(self):
        return self.name
    
    def get_info(self):
        print(self.name, self.location, self.dept)
    
emp1 = Employer()
emp2 = Employer("Venkat", "backend DEV")

emp1.get_info()# we can call the class methos by using the object
emp2.get_info()


emp2.location = "coimbatore" #by using the object we can use the class variables outside of the class
emp2.name = "Balaji"
emp2.get_info()
emp1.get_info()

##################################################################################################################

#......................Inheritance................

class User: #parent class
    location = "banglore"
    name = "Manjunath"
    role = "devOPS"

#class Company(User, Employer, ...etc..) we can inherit multiple classes - (i.e,) one class can have multiple parent class
class Company(User): #child class
    company_name = None
    company_location = None

    def __init__(self, name, location):
        self.company_location = location
        self.company_name = name



emp1 = Company("JFH", "Bangalore") #it is enough to create an object just for the child class
print(emp1.company_name)
print(emp1.name)# by using the child class object we can access the parent class



user1 = User()#but we cannot use parent class's object to access the child 
print(user1.name)
print(user1.company_name)


##################################################################################################################

#calling parent class's constructor by using child object
#using parent class's variables in child class

class User:
    location = None
    name = None
    role = None
    def __init__(self, name, role, location="Bangalore"):
        self.location = location
        self.name = name
        self.role = role
    

class Company(User):
    company_name = None
    company_location = None

    def __init__(self, name, role, location, comp_name, comp_location):
        super().__init__(name, role, location) #........................#we can user super() to call the parent class's constructor
        self.company_name = comp_name
        self.company_location = comp_location
    
    def all(self):
        return self.name, self.role, self.company_name


emp1 = Company("Manjunath", "LEAD", "Banglore", "JFH", "Balglore")

print(emp1.all())
