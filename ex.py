try:
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    result=a/b 
    print(result)
except ZeroDivisionError :
    print("Error ocourd")
except:
    print("Worng input")
else :
    print("invaled input")
finally :
    print("this will exsicute no matter what")