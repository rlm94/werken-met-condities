a = int(input("voer een getal in voor a1: "))
b = int(input("voer een getal in voor b1: "))

if a > b:
    print(f"a is het grootste getal: {a}")
    print(f"Het minimum is: {b}")
    print(f"Het maximum is: {a}")
elif a < b:
    print(f"a is het kleinste getal: {a}")
    print(f"Het minimum is: {a}")
    print(f"Het maximum is: {b}")
else:
    print("a en b zijn even groot")