def summation(l1):
    sum=0
    for i in l1:
        sum=sum+i
    print("Summation is : ",sum)

def searching(l1):
    search=int(input("Which Number do you want to find: "))
    found=0
    foundlist=[]
    for i in range(len(l1)):
        if l1[i]==search:
            found=found+1
            foundlist.append(i)
    if found==0:
        print("Not Found")
    else:
        print("{} Number items Found {} times".format(search,found))
    print("Found list is",foundlist)

def isPrime(num):
    count=0
    for i in range(2,11):
        if num%i==0:
            count=1
    if count==0:
        print("Prime")
    else:
        print("Not Prime")


# n=int(input("How Many Items ! :"))
# myList=[]

# for i in range(1,n+1):
#     i=int(input("Enter {} Number Items :".format(i)))
#     myList.append(i)

myNumber=int(input("Enter a Number to check isPrime : "))

# print(myList)
# summation(myList)
# searching(myList)
isPrime(myNumber)

# name=input("Enter Your Name : ")
# address=input("Enter Your Home Town : ")
# age=int(input("Enter Your Age: "))

# print("My name is {} and I am {} years old. I am from {}".format(name,age,address))