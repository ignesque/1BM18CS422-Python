class CallDetail:
    def __init__(self,calls):
        self.calls=calls
        self.fromcall,self.tocall,self.callspan,self.calltype=None,None,None,None
    def printDetails(self):
        for i in range(len(self.calls)):
            print(f"Call Detail {i+1}:")
            self.details=self.calls[i].split(",")
            self.fromcall=self.details[0]
            self.tocall = self.details[1]
            self.callspan = self.details[2]
            self.calltype = self.details[3]
            print(f"Called from:{self.fromcall}\nCalled to:{self.tocall}\nCall Duration:{self.callspan}\nCall Type:{self.calltype}\n")

class Util:
    def __init__(self):
        self.callobj = None

    def parseCustomer(self, callString):
        self.callobj=[CallDetail(callString)]
        return self.callobj
    def details(self,callobj):
        callobj[0].printDetails()


call = '9990000001,9330000001,23,STD'
call2 = '9990000001,9330000002,54,Local'
call3 = '9990000001,9330000003,6,ISD'
callString = [call, call2, call3]
callobj=Util().parseCustomer(callString)
Util().details(callobj)

