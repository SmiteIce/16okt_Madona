# string
vards = "Sveiki, pasaule! "
uzruna = 'Labrīt'
 # veselie skaitļi - integer
vecums = 30
skaits = 42
# desimāldaļskaitļi - float
cena = 19.99
attalums = 3.5
# saraksts - List
saraksts = [1, 2, 3, 4, 5]
vardadi = ["Anna", "Pēteris", "Māris"]
# korteža tipa mainīgie
koordinates = (3.14, 2.71)
krasas = ("sarkana", "zaļa", "zila")
# vārdnīcas tipa mainīgie - Dictionary
persona = {"vārds": "Jānis", "uzvārds": "Bērziņš", "vecums" 35}
students = {"vārds": "Anna", "uzvārds": "Krauze", "kursa_nr" 3}
# 3. piemers
#Izmantojot format metodi
vards="Eimija"
vecums=4
zinama_virkne="Mani sauc {} un man ir {} gadi."
print(zinama_virkne.format(vards,vecums))

#4.piemērs
#Izmantojot % operātoru (vecais veids, taču tas joprojām darbojas) vards = "Anna"
vecums = 30
zinama_virkne = "Mani sauc %s un man ir %d gadi." % (vards, vecums) print(zinama_virkne)