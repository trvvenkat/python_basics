#############################......................tuples............................#################################

numers = (1,2,4,4545,6,65,34534)

print(numers[:6])



num_dup = list(numers)
num_dup[1] = 200
numers = tuple(num_dup)
print(numers)



numers += (50, 10000)
print(numers)

del numers

#print(numers)