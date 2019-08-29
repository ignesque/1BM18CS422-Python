def order(arr, limit, flag='FALSE'):
    for i in range(0, limit-1):
        for j in range(i + 1, limit-1):
            if arr[i] > arr[j]:
                flag = 'TRUE'
    if flag == 'TRUE':
        print("Entered list is not ordered")
    else:
        checkvalue = int(input("\nEnter an element to be checked:"))
        check(arr, limit, checkvalue)


def check(arr, limit, checkvalue, flag='FALSE'):
    for i in range(0, limit):
        if arr[i] == checkvalue:
            print(f"Element {checkvalue} is found at position {i + 1}")
            flag = 'TRUE'
    if flag == 'FALSE':
        print("Element not found")


arr = list()
limit = int(input("Enter the range of list:"))
arr = [int(i) for i in input().split()]
if (len(arr) > limit):
    arr = arr[:limit]
print(f"Entered list is {arr}")
order(arr, limit)
