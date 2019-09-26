class CallDetail:

    def __init__(self, source, dest, span, type):
        self.callfrom = source
        self.callto = dest
        self.duration = span
        self.calltype = type

    def printDetails(self):
       print(f"Call From:{self.callfrom}\nCall To:{self.callto}\nCall Duration:{self.duration}\nCall Type:{self.calltype}\n")

class Util:
    def __init__(self):
        self.list_of_call_objects = []

    def parseCustomer(self, list_of_call_string):
        for calls in list_of_call_string:
            details = calls.split(",")
            obj = CallDetail(*details)
            self.list_of_call_objects.append(obj)

    def getDetails(self):
        for obj in range(len(self.list_of_call_objects)):
            print(f"Call Detail {obj+1}")
            self.list_of_call_objects[obj].printDetails()


call='9990000001,9330000001,23,STD'
call2='9990000001,9330000002,54,Local'
call3='9990000001,9330000003,6,ISD'

list_of_call_string = [call, call2, call3]
UtilObj=Util()
UtilObj.parseCustomer(list_of_call_string)
UtilObj.getDetails()
