class PhPay:
    def __init__(self,phNum,mainBal):
        self.__pn=phNum
        self.__bal=mainBal
        print(self.__bal,"5th line")

    
    def get_bal(self): # getter functiom for private varibles accessing
        # print(self.__bal,"8th line get_bal ()")
        return self.__bal
    
    
    def set_bal(self,inAmt): #setter function to update the main bal
        if inAmt<0:
            print("no negatuve amount can be sent")
        else:
            self.__bal+=inAmt  
            return self.__bal  
        

a=PhPay("123456789",150)
z=a.get_bal()
print(z)
y=a.set_bal(10000)
print(y)

# research points :
# how to access prvate varibles inside of a class