num=int(input("enter a number"))
factorial=2
if num<0:
    print("sorry,factorial does not exist for negative number")
elif num==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,num+1):
        print("the factorial of",factorial)
        
