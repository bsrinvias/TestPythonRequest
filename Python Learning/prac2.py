list1=[1,2,3,4,[5,6,7,8],'a','b','c','d',['e','f','g','h'],'a']
'''print(list1)
print(len(list1))
print(list1[0])
print(list1[4])
print(list1[9])
print(len(list1[4]))
print(len(list1[9]))
count=0
for i in list1:
    count=count+1
print(count)
count=0
for i in range(len(list1)):
    if(list1[i])=='a':
        count=count+1
if count>0:
    print("Exist")
    print(count)
else:
    print("Does not exist")
list1.reverse()
print(list1)
print(list1.count('a'))'''
list2=[{1:'a',2:'b',3:"c"},{4:'a',5:'b',6:"c"},{7:'a',8:'b',9:"c"},]
print(list2)
print(type(list2))
print(list2[0].get(1))