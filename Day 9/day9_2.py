#############################################.............FOR LOOP......................########################################

power_rangers = ["red", "blue", "yellow", "black"]

# i = 0
# while i<len(power_rangers):
#     print(power_rangers[i])
#     i += 1


for ranger in power_rangers: #forloop for lists
    for letter in ranger: #forloop for strings
        print(letter)
        


#########################################################################################################################


#working with break, continue in for loop
for ranger in power_rangers:
    #print("I AM "+ranger+" RANGER")
    if ranger=="blue":
        break
        #pass
        #continue
    print("I AM "+ranger+" RANGER")



for ranger in power_rangers: 
    for letter in ranger: 
        print(letter)
        if letter == "l":
            break #this will only get out of (LETTER) forloop

#########################################################################################################

for ranger in power_rangers:
    print("I AM "+ranger+" RANGER")
else:
    print("END OF POWER RANGERS")