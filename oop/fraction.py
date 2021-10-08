
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
    def gcd(self) :
        while self.dr != 0:
            m = self.nr % self.dr;
            self.nr = self.dr;
            self.dr = m;
        return self.nr;

    
a=Fraction(12,-6)
print(a.gcd())