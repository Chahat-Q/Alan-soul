def factorial(x):
    print(x)
    if x<=1:
        return x
    else:
        
        return (factorial(x-1) + factorial(x-2))

terms=int(input())
for i in range(terms):
    print(factorial(i))