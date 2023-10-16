# Cikla konstrukcijas
# 1. For cikls
saraksts=[1,2,3,4,5]
for elements in saraksts:
    print(elements)

# 2. Cikls for, apstrādājot veselu skaitļu intervālu
 # Intervāla norādīšanai tiek izmantoa funkcija rang.
a= int (input("Ievadiet skaitli!"))
s=0
for i in range(1, a+1):
    s+=i
print(s)
for i in range(10, 5, -2):
    print(i)

# 3. Cikls for, apstrādājot elementu kopumu.
burti=["aka", "paka", "laka"]
for i in burti:
    print("Sveiki, " + i +"!")

# 4. Cikls ar priekšnosacījumu while
s=0
a=int(input("Ievadiet skaitli:"))
while a>0:
    s+=a # s=s+a
    a=int("Nākošais skaitlis: ")
    print(s)

#While cikls izpildīs ciklu, kamēr dotā nosacījums ir patiess.
skaitlis=1
while skaitlis<=5:
    print(skaitlis)
    skaitlis+=1

# Cikla pārtraukšana un turpināšana !!!
saraksts=[1,2,3,4,5]
for elements in saraksts:
    if elements==3:
        continue # Pārtrauca šo iterāciju u nturpinām ar nākošo!
    if elements==5:
        break # Iziet no cikla, ja elemnts ir 5
    print(elements)

# Enumerate cikls
saraksts=['a', 'b', 'c']
for index, vertiba in enumerate(saraksts):
    print(f"Indekss ir: {index}, Vērtība: {vertiba}")

# uzdevums - izdrukāt visus pāra skaitļus robežās no 10 līdz 100, galapunktus ieskaitot!
# 1.risinājums
for skaitlis in range(10, 101):
    if skaitlis % 2==0:
        print(skaitlis)

# 2.risinājums
for skaitlis in range(10,101,2):
    print(skaitlis)

# For cikls ar sarakstu apstrādi
saraksts=[10,20,30,40,50]
rezultats=[] #tukšs saraksts
for skaitlis in saraksts:
    rezultats.append(skaitlis*2)
print(rezultats)

# While cikls ar lietotāja ievadi
ievade='' # simbolu virkne ir tukša
while ievade !="iziet":
    ievade=input("Ievadiet 'iziet' , lai pārtrauktu!")

# For cikls ar vairākiem sarakstiem /ZIP funkciju
vardi=["Anna", "Beta", "Gintars"]
vecumi=[25,30,35]
for vards, vecums in zip(vardi, vecumi):
    print(f"{vards} ir {vecums} gadus sens/sena")







