list1=[1,2,3,4,[5,6,7,8],'a','b','c','d',['e','f','g','h'],'a']
'''print(list1)
print(list1[0])
print(list1[4][0])
print(list1[9][0])'''
print(map(len, list1[9]))
counter=0
for i in list1:
    counter=counter+1
print(counter)

counter=0
for i in range(len(list1)):
    if list1[i]=='a':
        counter=counter+1
if counter>0:
    print("Exist")
    print(counter)
else:
    print("Does not exist")



