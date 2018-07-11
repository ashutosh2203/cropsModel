import numpy as np
import random, pylab

class hectareCrop(object):
    '''Used to project yearly yield for a crop based on fertilizer and rainfall 
    inputs.
    '''
    def __init__(self, NFert, irrigation):
	self.NFert = NFert
	self.irrigation = irrigation
	
        
    def rainfall(self):
        '''returns an annual rainfall amount based on normal probability distribution.
        Average rainfall during growth period is 50 cm and a standard deviation of 20 cm 
        return self.rainAmt
        '''
        self.rainAmt = random.gauss(50,20)
        #self.rainAmt = np.random.normal(50, 20,1000)
        return self.rainAmt
        

    def Nloss(self):
        '''Loss of N based on amount of rainfall that occurred.  For every cm of rain,
        3.0% loss of N occurs.
        Runs self.rainfall() to get self.rainAmt, returns an int of NAmt remaining based
        on yearly rainfall.  Int returned is not a object variable and does not replace
        self.NAmt
        '''
        self.NAmtRem = self.NFert - (self.NFert* 0.03 * self.rainfall())
        return self.NAmtRem
       
        
    def cropYield(self):
        '''Predicts the yearly yield of a crop based on rainfall and fertilizer
        inputs.
        Average yield is 100 bushels per acre based on average rainfall and 200 kg/ha
        per year N fertility.  A very basic model was used to predict yield where
        yield = rainAmt + (0.25 * N amt in kg/ha).  Need to use NAmt after rainfall
        for calcualtion.  
        RETURN: self.yearYield wich is the yield in bushels per acre
        '''
        self.yearYield = self.rainfall() + (0.25 * self.Nloss())
        return self.yearYield
        
    def profit(self):
        '''Assume $7 dollar per bushel yield.  However, a loss of $10 for each cm below 
        50 cm.  If irrigation is True, rainfall is supplemented up to 50 cm if it is 
        below.  If rainfall is 50 cm or greater, no additional irrigation takes
        place.
        RETURN grossProfit, not an object attribute
        '''
        if self.irrigation == True:
            self.NetProfit = 7 * self.cropYield()
        else:            
            if self.rainfall() >= 50:
                self.NetProfit = 7 * self.cropYield()
            else:
                self.NetProfit = 7 * self.cropYield() - 10*(50 - self.rainfall())
                
        return self.NetProfit


def modelYield(NFert, Irrigation= False, cycles = 10000):
    '''Model yield for 10,000 iterations and plot the yield in a histogram.
    '''
    YearYield = []        
    for x in range(10000):
        crop = hectareCrop(NFert, False)        
                
        YearYield.append(crop.cropYield())
        
    pylab.hist(YearYield)
    pylab.show()    
  
modelYield(200)
 
def modelProfit(NFert, cycles=1000):
    '''Model profit for 10,000 iterations for both irrigated and non-irrigated.
    Plot the predictions in four (2x2) subplot windows - histogram and boxplot for
    each of the data sets.
    '''
    YearProfit = []
    
    for sim in range(10000):
        crop = hectareCrop(NFert, False)        
                
        YearProfit.append(crop.profit())

    pylab.subplot(2,2,1)
    pylab.title('No irrigation')    
    pylab.hist(YearProfit)    
    pylab.subplot(2,2,3)
    pylab.boxplot(YearProfit, 0, '')
    
    YProfitIrr = []   
    for sim in range(10000):
        crop = hectareCrop(NFert, True)                       
        YProfitIrr.append(crop.profit())
        
    pylab.subplot(2,2,2)
    pylab.title('Irrigation')    
    pylab.hist(YProfitIrr)    
    pylab.subplot(2,2,4)
    pylab.boxplot(YProfitIrr, 0, '')
    pylab.show()
   
modelProfit(200)
    
#Uncomment to run
random.seed(1)
print("Unit Test 1") 
crop1 = hectareCrop(200, False) 
money = crop1.profit() 
print money #answer is 783.29
print crop1.yearYield #answer is 111.899
print crop1.rainAmt #answer 62.149
print crop1.NFert #answer is 200
print crop1.irrigation #answer is False
# 
# 
#print("Unit Test 2")
#crop2 = hectareCrop(100, True) 
#money = crop2.profit()
#print money #521.258
#print crop2.yearYield #74.465
#print crop2.rainAmt #49.715
#print crop2.NFert #100
#print crop2.irrigation #True
# 
