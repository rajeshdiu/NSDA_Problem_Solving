num=int(input("How many Item in List:"))
print("List Item Contain:",num)
newlist=[]
for i in range(num):
    i=int(input("Enter Number:"))
    newlist.append(i)
print("Your List is :",newlist)
evenlist=[]
oddlist=[]
for i in newlist:
    if i%2==0:
        evenlist.append(i)
    else:
        oddlist.append(i)
print("Even List is : ",evenlist)
print("Odd List is : ",oddlist)

print("Largest Number from newlist List using Max: ",max(newlist))
print("Largest Number from Even List using Max: ",max(evenlist))
print("Largest Number from oddlist List using Max: ",max(oddlist))

max=newlist[0]

for n in newlist:
    if n>max:
        max=n
print("Maximum Number from newlist is : ",max)

max=evenlist[0]
for n in evenlist:
    if n>max:
        max=n
print("Maximum Number from evenlist is : ",max)

max=oddlist[0]
for n in oddlist:
    if n>max:
        max=n
print("Maximum Number from oddlist is : ",max)