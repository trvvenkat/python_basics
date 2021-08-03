#########################.............LAMBDA FUNCTION.........############################

#regular function
def addition(a,b):
    return a+b

print(addition(2,5))



#lambda function
add2num = lambda a, b: a+b
#function_name = lambda (parameters): return value/operation
#other name of lambda func is anonymous function 
print(add2num(1,20))


#################################################################################################


#basic usage of lambda

#exponents() will return a lambda function which we can use to get the desiered output
def exponents(n):
    return lambda a : a**n



exp2 = exponents(2)
exp3 = exponents(3)

print(exp3(2))