from vehicle import Vehicle

class Car(Vehicle):
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
    
cr = Car(5, 9)
print(cr.fill_up_tank())