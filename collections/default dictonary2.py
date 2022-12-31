from collections import defaultdict
d=defaultdict(list)
l=[1,2,3,4,5,6]
for i in l:
    print(d[i])
    d[i].append(i)
    print(d[i])
d[2].append(d[2][0]+1)
print(d)

