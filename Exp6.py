class stringValidation:
    def __init__(self):
        self.open= ["[", "{", "("]
        self.close= ["]", "}", ")"]
    def validate(self,string):
        stack = []
        for char in string:
            if char in self.open:
                stack.append(char)
            elif char in self.close:
                pos = self.close.index(char)
                if len(stack) and (self.open[pos] == stack[-1]):
                    stack.pop()
                else:
                    return False
        if not len(stack):
            return True


sv=stringValidation()
string=input("Enter a string:")
check=sv.validate(string)
if check:
    print("The brackets are in order")
else:
    print("The brackets are not in order")
