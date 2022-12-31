from collections import defaultdict
d=defaultdict(int)
l=[1,2,3,4,5,6]
for i in l:
    print(d[i])
    d[i]=i+1
    print(d[i])
print(d)