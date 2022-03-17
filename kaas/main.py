cheesetype = input("is de kaas geel?").lower()

if cheesetype == "ja":
    holes = input("zitten er gaten in?").lower()
    if holes == "ja":
        price = input("Is de kaas belachelijk duur?").lower()
        if price == "ja":
            print("Emmenthaler")
        else:
            print("Leerdammer")
    else:
        stone = input("Is de kaas hard als steen?").lower()
        if stone == "ja":
            print("Pamigiano Reggiano")
        else:
            print("Goudse Kaas")
        
else:
    fungus = input("Heeft de kaas blauwe schimmels?").lower()

    if fungus == "ja":
        crust = input("Heeft de kaas een korst?").lower()
        if crust == "ja":
            print("Bleu de Rochbaron")
        else:
            print("Foume d'Ambert")
    
    else:
        nocrust = input("heeft de kaas een korst?").lower()
        
        if nocrust == "ja":
            print("Camembert")
        else:
            print("Mozzarella")
