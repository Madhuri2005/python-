def calculate_hcf(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while(True):
     if((greater %a==0)and(greater %b==0)):
        hcf=greater
        break
     greater+=1
    return hcf

num1=int(input("enter the value of x"))
num2=int(input("enter the value of y"))
print("the hcf of",num1,"and",num2,"is",calculate_hcf(num1,num2))
