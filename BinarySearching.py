n= int(input("Enter Items : "))
print(f"The list has {n} Items")

myList=[]
for i in range(n):
    i=int(input("Enter {} items :".format(i)))
    myList.append(i)

print("This is myList Without Sorting: ",myList)

for i in range(len(myList)-1):
    for j in range(len(myList)-1):
        if myList[j]>myList[j+1]:
            temp=myList[j]
            myList[j]=myList[j+1]
            myList[j+1]=temp
            
print("This is myList With Sorting: ",myList)

search=int(input("Which Number Do You Want to Found :"))
found=0
left,right=0,len(myList)-1

while left<=right:
    mid=(left+right)//2
    if myList[mid]==search:
        found=1
        break
    elif myList[mid]<search:
        left=mid+1
    else:
        right=mid-1
if found:
    print("Found")
else:
    print("Not Found")