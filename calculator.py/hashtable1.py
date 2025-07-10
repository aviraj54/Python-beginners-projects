class store:
    def __init__(self):
        self.a=[None] * 100
    def constore(self,data):
        code=data%10
        if self.a[code]==None:
            self.a[code]=data
        else:
            if self.a[code+1]==None:
                self.a[code+1]==data
            else:
                for i in range(100):
                    if self.a[i]==None:
                        self.a[i]==data
                        break
    def printdata(self):
        c=[]
        for i in range(100):
            b=self.a[i]
            if b!=None:
                c.append(b)
        print(c)
s1=store()
s1.constore(55)
s1.constore(56)
s1.constore(1)
s1.printdata()