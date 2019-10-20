print("Enter numbers to be added in the list:")
numlist=[int(num) for num in input().split()]
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
    
