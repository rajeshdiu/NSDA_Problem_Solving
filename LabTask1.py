s1 = int(input("Number for the List1 : "))
print(s1)

s2 = int(input("Number for the List2 : "))
print(s2)

List1=[]
for i in range(s1):
    i = int(input("Numbers for List1 :"))
    List1.append(i)
print(List1)

List2=[]
for i in range(s2):
    i = int(input("Numbers for List2 :"))
    List2.append(i)
print(List2)

newList = []
newList.extend(List1)
newList.extend(List2)
print("newList = ",newList)

newList.pop()
newList.pop()
print("After removing 2 last items newList = ",newList)

evenList = []
oddList = []

for i in newList:
    if i%2==0:
        evenList.append(i)
print("evenList = ",evenList)

for i in newList:
    if i%2!=0:
        oddList.append(i)
print("oddList = ",oddList)

min = newList[0]
for i in newList:
    if i <min:
        min = i
print("Minimum number from newList is : ",min)

#Here I have performed find out minimum number from a list

min=evenList[0]
for i in evenList:
    if i<min:
        min=i
print("Minimum number from evenList is : ",min)

min = oddList[0]
for i in oddList:
    if i<min:
        min=i
print("Minimum number from oddList is : ",min)