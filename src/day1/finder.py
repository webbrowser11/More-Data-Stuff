Data = ["bannana","strawberry", "orange","programmer"]
New_Data = []
Amn = 1

for i in Data:
    New_Data.append(Amn)
    Amn += 1

print(New_Data)
Amn_Ent = int(input("Above is some data connected to a list. you do not know what each item in the list is, but do know the numbers of that item. enter a number we will tell you what the item in the 'Data' list is: "))
Amn_Ent -= 1
print(Data[Amn_Ent])
if Data[Amn_Ent] == "programmer":
    print("You found the secret item")