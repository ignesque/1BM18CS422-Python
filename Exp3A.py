num=int(input("Enter a number to find its divisor:"))
div=list()
for factor in range(2,num+1):
    if num % factor == 0:
        div.append(factor)
if not div:
    print(f"{num} has no factors")
else:
    print(f"The factors of number {num} are {div}")