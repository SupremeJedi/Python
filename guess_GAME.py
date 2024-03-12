g_n=11
g_c=0
g_l=3
while g_c < g_l:
    g = int(input("Your guess : "))
    g_c += 1
    if g == g_n:
        print("You won")
        break
else:
    print("You lose")
    