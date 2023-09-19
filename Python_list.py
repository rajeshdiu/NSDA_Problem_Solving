
# myList=["Appple","Cherry","Kiwi","Banana","Guava"]
# myList2=["Red","Green","Yellow","Magenta"]
# myList.extend(myList2)
# print(myList)

# for i in myList:
#     print(i)
# myListLength=len(myList)
# myList2Length=len(myList2)

# print("First List Length is:",myListLength)
# print("First List Length is:",myList2Length)

# for i in range(myListLength):
#     print(myList[i])
# newlist=[]

# for i in myList:
#     if "a" in i:
#         newlist.append(i)

# print(newlist)

DaffodilBugs=["Pritom Sarkar","Shazid Hasan","Md. Fakrul Islam","Tahmina Sultana","Md.Milon Raza"]
DIPTIPydantic=["Joy Ahmed","MD Ahaduzzaman","Rupa Chakma","Al Arman Bejoy","MD Lokman"]
Pythoneers=["Ahnaf Tahmeed","Abrar Karim","Erfanul Haque","Farjana Tasnim","Sumiya Rasid"]
JSRMUnity=["Jilan Chowdhury","Mishan Kahisa","Sumaiya Akter Sima","MD. RASHEL MIA"]
Hungrybirds=["Ajoy Kumar Ray","Md. Rakib Ahmed Sazid","Md.Hasib","Mehedi Hasan","Faiad Farhan"]


teamlist=[DaffodilBugs,DIPTIPydantic,Pythoneers,JSRMUnity,Hungrybirds]
newlist=[] 

# for i in teamlist:
#     newlist.append(i)

# print(newlist)

for i in range(len(teamlist)):
    for j in teamlist[i]:
        newlist.append(j)

print(newlist)
# print(teamlist)

# print(teamlist)
# for i in DIPTIPydantic:
#     teamlist.append(i)
# print(teamlist)

# for i in Pythoneers:
#     teamlist.append(i)
# print(teamlist)

# for i in JSRMUnity:
#     teamlist.append(i)
# print(teamlist)

# for i in Hungrybirds:
#     teamlist.append(i)
# print(teamlist)

# teamlist.extend(DaffodilBugs)
# print(teamlist)
# teamlist.extend(DIPTIPydantic)
# print(teamlist)
# teamlist.extend(Pythoneers)
# print(teamlist)
# teamlist.extend(JSRMUnity)
# print(teamlist)
# teamlist.extend(Hungrybirds)
# print(teamlist)