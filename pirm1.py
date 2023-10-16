# uzdevums nr.2 - vairākiem nosacījumiem un funkciju, lambda

saraksts=[1,2,3,4,5,6,7,8,9,10] # masīvs

filtrets_saraksts=list(filter(lambda x: x%3==0, saraksts))

print("Pāra skaitļi sarakstā ", filtrets_saraksts)
saraksts=[1,2,3,4,5]

dublets_saraksts=list(map(lambda x: x*2, saraksts))

print("Dublēts saraksts:", dublets_saraksts)

skaitls=7


rez"Pozitīvs" if skaitlis>0 else "Negatīvs vao nulle"

print(nez)


x=10
y=20
lielaka=x if x>y else y
print(lielaka)
def noteikt_skaitlus(skaitlis1, skaitlis2):
      if skaitlis1>0 and skaitlis2>0:
        return "Abi skaitļi ir pozitīvi" elif skaitlis1<0 and skaitlis2<0:
    else:
        return "Abi skaitļi ir negatīvi" elif skaitlis1==0 or skaitlis2==0:
    else:
        return "Vismaz viens skait;is ir nulle"
    else:
        return "Skaitļi ir ar dažādām zīmēm ...."

sk1=int(input("Ievadi 1.skaitli:"))
sk2=int(input("Ievadi 2.skaitli:"))
rezultats=noteikti_skaitlus(sk1, sk2)
print(rezultats)

def validēt_vārdu
    if len(vards) <3:
      return "Vārds ir pārāk īss"
elif len(vards)>20:
      return "Vārds ir pārāk garš"
elif not vards.isalpha():
    return "Vārds drīkst saturēt tik burtus!"
else:
    return "Vārds ir derīgs!"

ievade=input("Ievadi savu vārdu: ")
