class car:
    def __init__(self,brand,color):
        self.brand=brand
        self.color=color
    def display(self):
        print("My car is a",self.brand,self.color)
c1=car("Toyota","Red")
c2=car("Honda","Blue")
c1.display
c2.display

