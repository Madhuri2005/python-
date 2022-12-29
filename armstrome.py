n=int(input("enter the number:"))

a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print("the number is an armstrong number")
else:
    print("the number is not an armstrong number")
