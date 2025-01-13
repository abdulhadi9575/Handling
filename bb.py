valid = False
try:
    a=int(input("Enter a number"))
    #enter a even number
    while a%2==0:
        print("bye")
        valid = True
except ValueError:
    print("invalid")