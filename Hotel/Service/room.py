class Room:
    def __init__(self,price,availablenumber): 
        self.price = price
        self.availablenumber=availablenumber
    
    def modifyprice(self,newprice):
        self.price=newprice
        
    def discountprice(self, discount=1):
        if discount < 0:
            return print("discount can't be negative")
        self.price*=discount
        
    def reduceroomnumber(self,reduceamount):
        if reduceamount > self.availablenumber:
            return print("not enough available room(s)")
        self.availablenumber-=reduceamount
        
    def addroomnumber(self,addamount):
        self.availablenumber+=addamount
        
    def display(self):
        return 'Price:{} Availablenumber:{}'.format(self.price, self.availablenumber)
        