teksts = input("Ievadi tekstu: ") #ievadam tekstu
def deleteCombo(teksts): #deklarējam funkciju, arguments - teksts 
  if teksts.count("abc")>0: #pārbaudām, vai ir kaut viena kombo "abc"
    teksts = teksts.replace("abc","") #aizvietojam "abc" ar ""
    print(teksts) #drukāt tekstu konsolē
  else: #pretējā gadījumā
    teksts = "Meklējamā kombinācīja netika atrasta!" #aizvietojasm tekstu ar pazīnojumu
    print(teksts) #drukāt tekstu konsolē
  return teksts #atgriežam vērtību teksts
deleteCombo(teksts) #arguments - teksts