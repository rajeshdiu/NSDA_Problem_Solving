myString=input("Enter List Seperate By Space: ")

print("You have Entered:", myString)

myList=[]

myList=[int(x) for x in myString.split()]

# for i in string.split():
#     myList.append(int(i))
    
print("This is my List :",myList)    

UniqueList=[]
DuplicateList=[]

#create a duplicate list
for i in range(len(myList)):
    for j in range(i+1, len(myList)):
        if myList[i]==myList[j]:
            DuplicateList.append(myList[i])

print("This is my Duplicate Item :",DuplicateList)

#create a unique list
for item in myList:
    if item not in UniqueList:
        UniqueList.append(item)

print("This is my Unique List :",UniqueList)

#sorting a list

for i in range(len(UniqueList)-1):
    for j in range(len(UniqueList)-1):
        if UniqueList[j]>UniqueList[j+1]:
            temp=UniqueList[j]
            UniqueList[j]=UniqueList[j+1]
            UniqueList[j+1]=temp

print("This is my sorted list: ",UniqueList)

#Binary Search

search=int(input("Which Item Do You Want to Search: "))
left=0
right=len(UniqueList)-1

found=False

while (left<=right):
    mid=(left+right)//2
    
    if UniqueList[mid]==search:
        found=True
        break
    elif UniqueList[mid]<search:
        left=mid+1
    else:
        right=mid-1

if found:
    print("Found")
else:
    print("Not Found")