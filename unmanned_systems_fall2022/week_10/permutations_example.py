from itertools import permutations 

start_location = (0,0)
perm = permutations([(1,2), (3,4), (6,6), (15,15)])


print("number of combinations is ", len(list(perm)))

# for i in list(perm):
#     print(i)


