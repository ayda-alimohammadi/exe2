users_count =input("Enter users count:")
count=int(users_count)
list =[]
thisdict ={}
for x in range(count):
    if x<=count:
        user_name = input("Enter user name:")
        user_age = input("Enter user age:")
        thisdict ={
            "name": user_name,
            "age": user_age,
        }
        list.append(thisdict)
    else:break
usere_search =input("enter name users:")
for y in list:
    if y["name"] ==usere_search:
        uage=y["age"]
        cont=+1
if count>=0:
    print(uage)
else:print("Errore")