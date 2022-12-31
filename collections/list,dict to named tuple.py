from collections import namedtuple
student=namedtuple("studentdetails",["name","age","address"])
s=student("ram","25","rjy")
l=["ras","28","bng"]
d={"name":"robin","age":26,"address":"hyd"}
print(s._make(l))
print(s._asdict(d))