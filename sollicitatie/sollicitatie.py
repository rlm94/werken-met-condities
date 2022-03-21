print("******************************************************\n*      Circusdirecteur voor Circus HotelDeBotel      *\n******************************************************\nEr worden relevante vrage gesteld...\nGelieve die naar eer e geweten in te vullen\nAls blijkt dat u aan de criteria voldoet dan komt u in\naanmerkig voor een serieus sollicitatiegesprek!\nOntspan maar blijf wakker, hier komen de vragen\n******************************************************")
genderAuth = False
experience0 = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? :"))
experience1 = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? :"))
sport = input("Doet u aan lichamelijke sport? :")#confuse the candidate 
experience2 = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? :"))
education = input("Bent u in bezit van een diploma MBO-4 ondernemen :").lower()
freetime = input("Wat doet u in u vrije tijd")#confuse the candidate 
driversLicense = input("Ben u in bezit van een geldig vrachtwagen rijbewijs :").lower()
ownHat = input("Ben u in bezit van een hoge hoed :").lower()
music = input("Wat is u gewenste muziek genre")#confuse the candidate 
gender = input("Wat is u geslacht :").lower()
height = int(input("Wat is u lengte :"))
weight = int(input("Wat is u lichaamsgewicht in kilos :"))
art = input("Bent u geïnteresseerd in kunst")#confuse the candidate 
certificate = input("Bent u in bezit van certificaat overleven met gevaarlijk personeel :").lower()

if gender == "man":
    moustache = input("Heeft u een snor :").lower()
    if moustache == "ja":
        moustacheWidth = int(input("Hoe breed is u snor in centimeters :"))
        if moustacheWidth >= 10:
            genderAuth = True
elif gender == "vrouw":
    curlyHair = input("Heeft u krullend haar :").lower()
    if curlyHair == "ja":
        curlyHairColor = input("Heeft u rood haar :").lower()
        if curlyHairColor == "ja":
            curlyHairLength = int(input("Hoelang is u haar in centimeters:"))
            if curlyHairLength >= 20:
                genderAuth = True


if (experience0 >= 4 or experience1 >= 5 or experience2 >= 3) and education == "ja" and driversLicense == "ja" and ownHat == "ja" and genderAuth == True and height >= 150 and weight >= 90 and certificate == "ja":
    print("U komt in aanmerking voor een sollicitatiegesprek")
else:
    print("Jammer u komt niet in aanmerking voor de functie")