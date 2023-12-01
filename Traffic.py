class BikeShop:
    def __init__(self,stock,):
        self.stock=stock
    def displayBike(self):
        print("Total available bike is",self.stock, "for Rent")
    def Rent_for_Bike(self,Qty):
        if Qty<=0:
            print("Please enter valid input")
        elif Qty>self.stock:
            print("Enter value in Range")
        else:
            print("Total number of bike",Qty*1000)
            print("Total Bike",self.stock-Qty)
while True:
    obj=BikeShop(100)
    User_input= int(input('''
    1 Total number of bike in Stock:--
    2 Bike on rent
    3 Exit
    '''))
    if User_input==1:
        obj.displayBike()
    elif User_input==2:
        n=int(input("Enter the Qty"))
        obj.Rent_for_Bike(n)
    else:
        print("Sorry no bike chooses")
        break
