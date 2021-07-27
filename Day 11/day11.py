######################.................... Functions... recursions...........##############################


number = 3
result = 0
#basic execution of FOR LOOP
for n in range(1,number+1):
    #print(n)
    result = result + n

print("...........................")
print(result)




#instead of the above loop, we can use the following function (recursions / funtion recursions)
#to understand the flow, i've attached a image, please refer that
def rec_example(num):
    print(num)
    if num>0:
        result = num+rec_example(num-1)
        print(result)
    else:
        return num
    return result




number = 5

print(rec_example(number))