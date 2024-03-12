import random

choice = input('Choose(Odd/Even):')

num1 = random.randint(1, 10)

num2 = int(input('Enter No:'))

add = num1 + num2

print(f'''
You chose: {choice}
Your number : {num2}
Computers number : {num1}
Sum = {add}''')

if add/2 % 1:
    print(f'''
    {add} = Odd
    Odd wins''')
else :
    print(f'''
    {add} = Even
    Even wins''')