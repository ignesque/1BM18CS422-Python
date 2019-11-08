def reverse(str):
    print(f"\nEntered string is \'{str}\'")
    divstr = str.split(" ")
    ogstr=" "
    divstr.reverse()
    ogstr=ogstr.join(divstr)
    print(f"Reverse of original string is \'{ogstr}\'")
def reverseString(str):
    str = str.split()
    strlist = ""
    print("Reverse of each word is ")
    for i in str:
        strlist += i[::-1]
        strlist += "\n"
    print(strlist)
string = input("Enter a string:")
reverse(string)
reverseString(string)

