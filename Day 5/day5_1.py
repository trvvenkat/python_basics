###############....................................List operations and handling.............................########################################

members = ["manunath", "shankar", "venkat", "charan", "gokul", "pooja", "suchitra", "kajal", "thulasi"]

print("...................using value assign method...............")
#assigning values one by one in the list
for member in members: #1st time index 0, 2nd time index 1, ..... nth time index is n-1
    print(member)


print("................using for loop....................")



#assigning values based on index values using loop

print(range(len(members))) #range(n, m)  n = starting value(default value is 0), m = ending value +1

for index in range(len(members)):
    print(members[index])



print(".................using while loop......................")
index = 0
while index < len(members):
    print(members[index])
    index = index + 1


print(".................................................................")

[print(member) for member in members]  #list comprehension - not storing into any variable

############################################################################################################################################

#without list comprehension
without_lc = []
for i in range(3, 9):
    without_lc.append(members[i])
print(without_lc)


#with list comprehension
tech = [members[i] for i in range(3, 9)]  #list comprehension - storing the new list to a variable
print(tech)

#syntax:     newlist = [(expression/value/variable) for (value/expression/variable) in (old list/iterator) if (condition)]

names_with_m = [name for name in members if "m" in name] #list comp with if condition
print(names_with_m)


numbers = [1,2,3,4,5,6,7,8,9,10]
new_num = [number if number > 5 else number+5 for number in numbers] #list comprehension with if else
print(new_num)

#############################################################################################################################
#soring lists
members.sort() #ascending
print(members)

members.sort(reverse=True)
print(members)

test_list = ["aa", "ab", "za", "cC", "ca"]
test_list.sort(key=str.lower)
print(test_list)

#################################################################################################################################

#list copy

a = 5
num = a

new_members = list(members)
new = new_members.copy()
print(new)

print(new_members)


########################################################################################################################

#joining 2 lists
new_mem = ["shilpa", "neha"]

# for new in new_mem:
#     members.append(new)
members += new_mem
print(members)