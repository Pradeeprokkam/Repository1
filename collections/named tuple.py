from collections import namedtuple
student=namedtuple("studentdetails",["name","age","address"])
s=student("ram","25","rjy")
print(s.name)
