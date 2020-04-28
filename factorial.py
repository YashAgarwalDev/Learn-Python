def factorial(x):
    return 1 if(x == 1 or x==0) else x * factorial(x -1)
    num = 5
    print("Factorial of", num, "is", factorial(num))