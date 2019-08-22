numlist=[]
print("Enter numbers to be added in the list")
while True:
    num=int(input())
    if num != -1:
        numlist.append(num)
    else:
        break
evenlist=[]
for even in numlist:
    if even % 2 == 0:
        evenlist.append(even)
print("The numbers in the first list are",end=" ")
for num in numlist:
    print(num,end=" ")
print("\nThe even numbers in the list are",end=" ")
for num in evenlist:
    print(num,end=" ")
