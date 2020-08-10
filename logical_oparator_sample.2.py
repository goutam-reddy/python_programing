weight = int(input("enter your weight ---> " ))
unit = input("(L)bs or (K)g ---> ")
if unit.upper() == "K":
    weight_lbs = weight / 0.45
    print("your weight in lbs is --->", weight_lbs)
elif unit.upper() == "L":
    weight_kg = weight * 0.45
    print("your weight in kg is --->", weight_kg)
