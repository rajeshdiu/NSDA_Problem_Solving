list1=[]
list2=[]
for i in range(8):
    i=int(input("Enter Items: "))
    list1.append(i)
print(list1)
for i in range(8):
    i=int(input("Enter Items: "))
    list2.append(i)
print(list2)

newlist=[]

newlist.extend(list1)
newlist.extend(list2)
print(newlist)
# del newlist[-2:]
newlist.pop()
newlist.pop()
print(newlist)

Evenlist=[]
Oddlist=[]

for i in newlist:
    if i%2==0:
        Evenlist.append(i)
    else:
        Oddlist.append(i)
print("My Even list is: ",Evenlist)
print("My Odd list is: ",Oddlist)

min1=newlist[0]

for n in newlist:
    if n<min1:
        min1=n
print("Minimum Number from newlist is : ",min1)

min2=Evenlist[0]
for n in Evenlist:
    if n<min2:
        min2=n
print("Minimum Number from Evenlist is : ",min2)
min3=Oddlist[0]
for n in Oddlist:
    if n<min3:
        min3=n
print("Minimum Number from Oddlist is : ",min3)