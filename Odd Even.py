# Using While with if and Else Loop

x = int(int(input("\n Declare your number\n")))
i = 1
while i < x:
    if (i % 2 == 0):
        print("\nYes this an even\n", i)
    else:
        print("\nThis is an odd number \n", i)
    i += 1        
