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
a=Fraction(5,-4)
print(a.fr())