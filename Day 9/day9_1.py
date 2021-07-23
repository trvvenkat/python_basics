#################################################.................LOOPS.........................####################################

# while (condition):
#     execute the code in loop

i = 5
while i<10: #make sure you change the condition once the loop is iterated once before the next iteration (else it will be an infinite loop)
    i += 1
    print(i)
    #i += 1


################################################################################################################################

#pass, break, continue statements

i = 1
while i < 10:
    print(i)
    if i == 3:
        print("inside checking for 3")
        break # ----- this will break the entire loop and come out of it
        #pass # ----- passes (flags) the if condition tree
        #continue # ---- when using continue, it will again redirects us to the start of the loop without executing the rest below the continue
    print("Iteration is happening")
    i += 1


print("LOOP ENDED")

##################################################################################################################################

i = 1


while i < 10:
    print(i)
    print("Iteration is happening")
    i += 1
else: #in python we have else(similar to IF CONDITION) for while loop.... this will execute once the while(condition) is failed
    print("LOOP ENDED....")