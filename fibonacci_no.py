def fib(n) :
    if( n <= 1):
        return n
    else:
        return(fib(n-1)+fib(n-2))
    

n = float(input("Enter your number :"))
newn = (fib(n))
print(newn)
