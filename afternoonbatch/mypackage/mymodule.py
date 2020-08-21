class calc:
    def add(n1,n2):
        return n1+n2
    def sub(n1,n2):
        return n1-n2
    
    
    
    
class Math:
    def Even(num):
        if num%2==0:
            return True
        else:
            return False
    def Odd(num):
        if num%2!=0:
            return True
        else:
            return False
        
        
class mycalc:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def __add__(self):
        return self.n1+self.n2
    def __sub__(self):
        return self.n1-self.n2
    