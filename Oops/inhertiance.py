class V1:
    def __init__(self,message,dp):
        self.message    = message
        self.dp         = dp

    def display(self):
        print(self.message)
        print(self.dp)

class V2(V1):

    def __init__(self, message, dp,status,audiocall):
        super().__init__(message, dp)
        self.status         = status
        self.audiocall      = audiocall

    def display(self):
        V1.display(self)
        print(self.status)
        print(self.audiocall)

class V3(V2):
    
    def __init__(self, message, dp,status,audiocall,AI,payment):
        V2.__init__(self,message, dp,status,audiocall)
        self.status     =   AI
        self.audio      =   payment

    def display(self):
        V2.display(self) 


obj = V3("Hi", "No","Good Morning","30-min","yes","2000$")
obj.display()
