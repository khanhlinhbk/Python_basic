
class Fraction:
    def __init__(self,nr,dr) :
        if(dr>0):
            self.nr=nr
            self.dr=dr
        else:
            self.nr=-nr
            self.dr=-dr
        
    @property
    def nr(self):
        return self._nr
    @property
    def dr(self):
        return self._dr
    @dr.setter
    def dr(self,dr):
            self._dr=dr
    @nr.setter
    def nr(self,nr):
            self._nr=nr
    def fr(self):
        return (str(self.nr)+"/"+str(self.dr))
    def hcf(self) :
        while self.dr != 0:
            m = self.nr % self.dr
            self.nr = self.dr
            self.dr = m
        return self.nr
    def reduce(self):
        x = self.nr
        y = self.dr
        while self.dr != 0:
            m = self.nr % self.dr
            self.nr = self.dr
            self.dr = m
        if(int(y/self.nr) == 1):
            return str(int(x/self.nr))
        return (str(int(x/self.nr))+"/"+str(int(y/self.nr)))
        
    def __add__(self,other):
        if isinstance(other, int) or isinstance(other, float)  :
            z = self.dr*other+self.nr
            return (str(z) +"/" +str(self.dr)) 
        elif isinstance(other, Fraction):
            z = self.dr*other.nr+ self.nr*other.dr
            return (str(z)+"/"+ str(other.dr*self.dr))
        else : return("Nhập đúng định dạng")
    
a=Fraction(12,-6)
b=1.5
print(a+b)