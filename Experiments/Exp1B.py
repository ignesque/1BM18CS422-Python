def fibonacci(num):
    fiblist=[]
    num1=0
    num2=1
    if num==0:
        print("Invalid Number")
    elif num==1:
        fiblist.append(num1)
    elif num==2:
        fiblist.append(num1)
        fiblist.append(num2)
    else:
        fiblist.append(num1)
        fiblist.append(num2)
        for fibnum in range(2,num):
            num3=num1+num2
            num1=num2
            num2=num3
            fiblist.append(num3)
    for fibnum in fiblist:
        print(fibnum,end=" ")
print("How many fibonacci numbers to generate:",end="")
num1=int(input())
fibonacci(num1)
