n=int(input("Enter How Many Items : "))
print(f"Your List Contain {n} Items : ")

myList=[]

for i in range(n):
    i=int(input("Enter {} Item : ".format(i+1)))
    myList.append(i)

print("This is My List Items : ",myList)

found=0

search=int(input("Which Number Do You Want to Search: "))

print("Your Search Item is {}".format(search))

myIndex=[]

for i in range(len(myList)):
    if myList[i]==search:
        found=found+1
        myIndex.append(i)
if found:
    print("{} found {} times at index {} ".format(search,len(myIndex),myIndex))
else:
    print("Not Found")