
gp=[7980,22349,999,2799,229900,11101,9999,2195,9800,4999]
gp.sort()

emp=4
diff=[]
for i in range(len(gp)-emp):
    diff.append(gp[i+emp-1]-gp[i])
min_v=min(diff)
min_index=diff.index(min_v)
print("Number of the employees : 4")
for i in range(min_index,min_index+emp):
    print(gp[i])



# print("minimum value id"+str(min_v))
emp=6
diff=[]
for i in range(len(gp)-emp):
    diff.append(gp[i+emp-1]-gp[i])
min_v=min(diff)
min_index=diff.index(min_v)
print("Number of the employees : 6")
for i in range(min_index,min_index+emp):
    print(gp[i])


emp=2
diff=[]
for i in range(len(gp)-emp):
    diff.append(gp[i+emp-1]-gp[i])
min_v=min(diff)
min_index=diff.index(min_v)
print("Number of the employees : 2")
for i in range(min_index,min_index+emp):
    print(gp[i])