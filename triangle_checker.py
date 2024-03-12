A = float(input('first angle: ')) 
B = float(input('second angle: ')) 
C = float(input('third angle: ')) 

asp = A +B+C
if asp !=180:
    print('no triangle')
else:
    if A < 90 and B < 90 and C < 90:
        print('It is an acute angle triangle')
        
    elif A > 90 or B > 90 or C > 90:
        print('It is an obtuse triangle')
    elif A == 90 or B == 90 or C == 90:
        print('Right angle triangle')
    else:
        pass

