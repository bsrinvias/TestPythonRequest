class computer:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def config(self):
        print(self.a,self.b,self.c)
comp1=computer(1,2,3)
#comp2=computer(4,5,6)
comp1.config()
#comp2.config()