

name = "manjunath"
n = 5

print(name[:n]) #getting first n characters from a string (index_value:no_of_characters)
print(name[1:n])
print(name[-1])

#############################################################################################


print(name.upper()) #this converts everything to upper case
print(name.lower()) #this converts everything to lower case
print(name.title()) #this converts the 1st letter of the word in upper case
print(name)



bad_venkat = "i am veryyy baddd         "
print(bad_venkat+"check space")
print(bad_venkat.strip()+"check space") #strip() removes all the vacant spaces left at the end of the string



a = "appne"
a_fixed = a.replace("n", "l")
print(a.replace("p", "l")) #it replaces whever we say  variable.replace("what char to replace", "replacement char") (NOTE: this will affect all the occurences)
print(a)
print(a_fixed)



hobbies = "music, movies, tech, cricket, basketball"
print(hobbies.split(", "))  #variable.split("delimitor") 

############################################################################################################################

fruit1 = "apple"
fruit2 = "orange"
str2 = "is good for health"
sen = fruit1+" "+str2 #we can combile multiple strings in python

print(sen)

print(fruit1+" "+str2)

#######################################################################################################


template = "{} is very bad {} {}" #format() method to replace something in a given string
who = "venkat"
print(template.format(who, "good", "bad"))


about_me = "i am {} years old"
age = 100
print(about_me.format(age))


sen2 = "i bought a {2} for {1} at {0}"

print(sen2.format("LA","$1000","phone"))


str2_revised = "{2} is good for health"
print(str2_revised.format("apple", "orange", "pineapple"))


###############################################################################################################


print(" \"MANJUNATH\"  ") #  "MANJUNATH" -->   \"message\"


person_1 = "\n i talked with venkat and he said \"manjunath is bad\"" #example for escape sequence
print(person_1)

##############################################################################################################

smaple_str = "this is a SAMPLE string"

print(smaple_str.title()) #.title() will convert 1st letters of every word in the string to uppercase
print(smaple_str.capitalize()) #this will only convert the 1st letter of the 1st word of the string to uppercase
print(smaple_str.islower()) #checks and returns true if all the char given is lowercase