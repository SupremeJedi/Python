weight = int(input("Wieght:"))
unit = input("(L)bs or (K)g :")
if unit.upper()== "L":
    wieght_in_kg = weight*0.45
    print = (f"{wieght_in_kg}Kg is your wieght ")
elif unit.upper()== "K":
    wieght_in_pound = weight*2.2
    print(f"{wieght_in_pound}Lbs is your wieght")

