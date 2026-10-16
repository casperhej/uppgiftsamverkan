print ("välkommen till programmeringens samhällspåverkan under 1900 och 2000 talet")

points = 0

print("""vilket år introducerades hållkort för att programmera tidiga datorer")
A: 1900-talet
B: 1850-talet
C: 2000-talet
D: 1800-talet
""")

answer1 = input("Skriv ditt svar (A, B, C eller D) :")

if answer1.upper() == "A": 
    print ("Rätt svar! Hållkort introducerades under 1900-talet!")
    points += 1
else:
    print ("fel svar. rätt svar är A: 1900-talet.")

print ("du fick", points, "poäng.")


print(""""Vad heter kvinnan som skapade den första algoritmen
A: Marcus Hoppins
B: Einstein
C: Sven Svensson
D: Ada Lovelace
""")

answer2 = input("skriv ditt svar (A, B, C eller D) : ")

if answer2.upper() == "D":
    print ("Rätt svar! Ada Lovelace var den första programmeraren")
    points += 1
else: 
    print("fel svar. Rätt svar är D: Ada Lovelace")

print ("du fick", points, "poäng.")

print("""Vilka var det som oftast arbetade med programmering?

A: män
B: kvinnor
C: Kungligheten
D: Adeln
""") 

answer3 = input("skriv ditt svar A, B, C eller D): ")

if answer3.upper() =="B":
    print("rätt svar! Kvinnor.")
    points +=1
else: 
    print("fel svar ditt pucko. Rätt svar är B: kvinnor")

print ("du fick", points, "poäng.")

print ("""Vem ledde apollo programmets mjukvaruutveckling?
A: Brad Pitt
B: Nooshi Dadgostaar
C: Margaret Hamilton
D: Ava Legloose
""")

Answer4 = input("skriv ditt svar (A, B, C eller D) : ")

if Answer4.upper() == "B": 
    print("Rätt svar! Margaret Hamilton ledde mjukvaruutvecklingen för Apollo Programmet.")
    points +=1
else:
    print ("fel svar. Rätt svar är B: Margaret Hamilton")

print("du fick", points, "poäng.")

print("""hur började pc revolutionen?
A: Genom att datorer blev sämre
B: Genom att datorer blev fulare
C: Genom att datorer blev snabbare
D: Genom att datorer blev mindre och billigare
""")

answer5 = input("Skriv ditt svar (A, B, C eller D): ")

if answer5.upper() == "D": 
    print("Rätt svar Pajjas! PC revolutionen började faktiskt när datorer blev mindre och billigare!")
    points +=1
else:
    print("Fel svar pajjas! Rätt svar är D: Genom att datorer blev mindre och billigare")

print ("du fick", points, "poäng.")

print ("Hoppas det gick bra för dig under denna svåra QUIZ, och tack för att du deltog i quizet! Du fick totalt ", points, "poäng.") 



    

