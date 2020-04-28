salary = int(input("Enter salary"))
noy = int(input("Enter the year"))
if(noy > 5):
    x = salary * 5 / 100
    salary += x
    print("you get your salary", x)
    print("now after bonus you got", salary)
else:
    print("sorry u can't get bonus")    
