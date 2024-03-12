numbers =  [ 4,42,5,5,1,6,7,6,7,4,3,2,2,4]
uniques = []
for number in  numbers:
    if number not in uniques:
        uniques.append(number)
print(f"{uniques}")