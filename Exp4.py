class Student():
    def __init__(self):
        self.__marks, self.__age, self.__id = None, None, None

    def validateMarks(self):
        if 0 <= self.marks <= 100:
            return True
        else:
            return False

    def validateAge(self):
        if self.age > 20:
            return True
        else:
            return False

    def checkQualification(self):
        if self.marks >= 65:
            return True
        else:
            return False

    def setDetails(self):
        print(f"\nStudent ID is {self.id}\nAge is {self.age}\nMarks Scored is {self.marks}\n")

    def getDetails(self):
        self.id = input("Enter Student ID:")
        self.age = int(input("Enter Student Age:"))
        self.marks = int(input("Enter Marks Scored:"))
        if self.validateMarks() and self.validateAge():
            if self.checkQualification():
                return True
            else:
                print("\nStudent not Qualified")
        else:
            print("\nMarks or Age is invalid")
            return False


st = Student()
if st.getDetails():
    st.setDetails()
    print("Admission Successful")
else:
    print("Admission Failed")
