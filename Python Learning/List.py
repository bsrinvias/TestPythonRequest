list1=[1,2,3,4,[5,6,7,8],'a','b','c','d','a',['e','f','g','h']]
print(list1)
print(len(list1))
print(list1[4])
print(list1[4][2])
print(list1[10])
print(len(list1[4]))
list2=[{1:'a',2:'b',3:'c'},{4:'d',5:'e',6:'f'},{7:'h',8:'i',9:'j'}]
print(list2)
print(list2[0].keys())
print(list2[1].values())
list2.reverse()
print(list2)
print(len((list2)))
count=0
for i in range(len(list1)):
     if(list1[i])=='a':
      count = count + 1
if count>0:
    print("Count of repeated item:",count)
    print("Exist")
else:
    print("Does not exist")
x=[i for i in range(10)]
print(x)
x=[i for i in 'abcde']
print(x)
x=[i for i in range(10)]
print(x[0])
x=[i for i in 'abcde']
print(x[0])
x=[i for i in range(10) if i % 2==0]
print(x)
x=[i for i in range(10) if i %2==1]
print(x)

list1=[1,2,3,4,[5,6,7,8],'a','b','c','d',['e','f','g','h'],'c']
print(len(list1))
counter=0
for i in list1:
    counter=counter+1
print(counter)

