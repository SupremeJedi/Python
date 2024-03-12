amount= int(input('enter total bill:'))
gender = input('male or female ')
if amount > 10000:
    if gender == 'female':
        print('smth')
        final_bill = amount
        print(final_bill)
    else:
        print('no disc')