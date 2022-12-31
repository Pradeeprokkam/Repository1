from collections import ChainMap
a={1:2,2:3,3:4,4:5}
b={10:11,11:12,12:13,13:14}
c={20:21,21:22,22:23,23:24}
d=ChainMap(a,b,c)
print(d)
#you can add another dictionary wit new_child
e={30:31,32:33,33:34,34:35}
print(d.new_child(e))