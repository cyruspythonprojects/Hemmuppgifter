#Deklaration av viktiga variabler, listor och dictionaries.
student_year = 1
avg_grade = 0
courses = ['Svenska','Engelska','Matematik','Programmering','Datorkunskap']
grade_values = {'IG':0,'G':1,'VG':3,'MVG':5}


#Våran "huvudloop" som har årskursen som condition.
while student_year < 4:
    #Här nollställer vi genomsnittsbetygen innan fösta genomräkningen.
    avg_grade = 0    
    print("\nStudenten går i åk:",student_year,"\n")
    for i in grade_values.keys():
        print(i,'=',grade_values[i],"poäng.")
    print("")
    #Våran felhantering för inputen i loopen.    
    try:
        #Använder en for-loop för att gå igenom alla kurser samt dictionaryn för att hämta värden för respektive betyg.    
        for i in courses:
            #har en upper här (nedan) eftersom keys:en i dictionaryn är uppercase, men med upper() funktionen, så spelar det ingen roll om det är stor eller liten bokstav.
            user_input = input("Vad får eleven i " + i + ": ").upper()
            avg_grade += grade_values[user_input]
            print(user_input,":",grade_values[user_input])
    except:
        print("Fel input, var god och skriv endast: IG , G , VG , MVG .")
        #Har en continue här för att starta om loopen från "början" så att säga, eftersom if-statsen
        #inte hinner köras så förblir student_year den samma och loopen börjar om från "där den va"
        #d.v.s. man börjar om från början att skriva in betyg för den årskursen loopen är i.
        continue
    
    #Får ut genomsnittsbetyget och printar detta.
    avg_grade /= 5
    print("\nGenomsnittsbetyg:",avg_grade,"\n")
        
    #If-satsen som avgör om man går vidare eller inte, och om man får en femma så får man också en "bonus-utskrift."
    if avg_grade <= 1:
        print("!!! Du får tyvärr gå om detta år !!!")
    elif avg_grade > 1:
        student_year += 1
        #Lägger in if-satsen i en if-sats så att man minskar redundans genom att skriva en egen elif för specialfallet.
        if avg_grade == 5:
            #Specialutskrift om man har fått fullpott - alla MVG.
            print("*** Grattis, ALLA MVG, du får en guldstjärna! ***")
        print("### Grattis, du avancerar till nästa år! ### \n")
        #En avskiljare (med tecken) så det blir mer läsbart i output.
        print("------------------------------------------------------------------------------\n")
    else:
        #Ett pythonistisk 'avslut' på våran if-sats som inte kan hamna i else-blocket, därför har vi bara en 'pass'.
        pass