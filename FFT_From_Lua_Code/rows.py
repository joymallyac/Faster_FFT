
import random,math

samples = 50

class Data:

    def __init__(self):
        self.w = {}
        self.syms = {}
        self.nums = {}
        self.clss = None
        self.rows = []
        self.name = []
        self._use = {}
        self.indeps = {}

    """ These are the independent columns """
    def indep(self, c):
        return self.w.get(c) is None and self.clss != c
    
    """ These are the dependent columns """
    def dep(self, c):
        return not self.indep(c)    

    
    def dom(self, row1, row2):
        n = len(self.w)
        s1 = 0
        s2 = 0
        for c, x in self.w.items():
            a = numNorm(self.nums[c], row1[c])
            b = numNorm(self.nums[c], row2[c])
            s1 = s1 - 10**(x * (a-b)/n)
            s2 = s2 - 10**(x * (b-a)/n)
        return s1/n < s2/n


    def doms(self):
        n = samples
        self.name.append(">dom")
        for row1 in self.rows:
            row1.append(0)
            for i in range(0,n):                
                row2 = self.rows[random.randint(0,len(self.rows) -1)]            
                if(row1==row2):
                    continue
                if(self.dom(row1, row2)):
                    row1[-1] += 1/n
        self.w[len(self.name)-1] = 1     
       


def numNorm(num, x):
    hi = num.hi
    lo = num.lo
    return (x - lo)/(hi - lo)


