dic={1:"a",2:"b",3:[1,2,3,4],4:{"a","b","c"}}
print(dic[4])
print(type(dic))
print(dic)
print(dic.keys())
print(dic.values())
print(list(dic.values())[0])
print(list(dic.keys())[0])
print(dic.get(3)[1])
print(dic.get(4))
if 1 in dic:
    print("exist")
else:
    print("does not exist")

a=dic.get(2)
if a=="b":
    print("exist")
else:
    print(("Not exist"))