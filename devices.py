#This is the first class
class Device(): #This defines the common attributes of devices 
    def __init__(self, brand, model, year, color, ram, storage, battery, battery_charge ):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color 
        self.ram = ram
        self.storage = storage
        self.battery = battery
        self.battery_charge = battery_charge

    def __str__(self):
        return f'{self.brand} {self.model} '
    def reduce(self):
        self.battery_charge = self.battery_charge - 1

class Mobile (Device): #This defines the attributes of a mobile
    def __init__(self, brand, model, year, color, ram, storage, battery,battery_charge, camera):
            super().__init__(brand, model,  year, color, ram, storage, battery, battery_charge)
            self.camera = camera

    def on(self):
        print('Welcome :)')
    def __str__(self):
        return super().__str__() + f'({self.year}) '\
            f'({self.color}, '\
            f'{str(self.ram)}GB RAM, {str(self.storage)}GB Storage)'\
            f' with {str(self.camera)} Cameras and {str(self.battery)}mAh Battery \n'\
            f'Battery Now - {str(self.battery_charge)} \n\n\n'
