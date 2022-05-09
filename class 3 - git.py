class Vehicle:

    def __init__(self, make,model):
        self.make= make
        self.model = model
        
    
    def describe_vehicle(self):
        print (Vehicle.__dict__)


class Car(Vehicle):
    def __init__(self,make,model):
        super().__init__(make,model )
        self.doors = input("enter doors: ")
        self.cruise = input( 'do you need cruise controle? ')
        self.ABS = input( 'do you need ABS? ')
        self.self_drive = input('do you need self drive? ')

    def describe_vehicle(self):
        print (f' you have a '+self.make)
        print (f' your '+self.model +' is a '+ self.make)
        print (f' your '+self.model + ' has '+ self.doors + ' doors')
        print (f' cruise : ' +  (self.cruise) + ' , ' + 'ABS : ' + (self.ABS) + ' self drive : ' + self.self_drive)
class Pickup(Vehicle):
    def __init__(self,make,model):
        super().__init__(make,model)
        self.bed_length = input("enterbed_length: ")
        self.power_mirror = input( 'do you need power mirrors? ')

    def describe_vehicle(self):
        print (f' you have a '+self.make)
        print (f' your '+self.model +' is a '+ self.make)
        print (f' your '+self.model + ' has '+ self.bed_length + ' inches bed_length')

i = input ("Enter 1 for car, 2 for pickup and 3 for quit: ")
i = int(i) 
status = True 
while status and i != 3:
    make = input("make:")
    model = input ("model:")
    if i == 1 :
        
        mycar=Car(make,model)
        mycar.describe_vehicle()
        print (mycar.__dict__)
        x= input ("Do you want to try again? y/n: ")
        if x == "n":
            break
        i = input ("Enter 1 for car, 2 for pickup and 3 for quit.")
        i = int(i)  
        

    elif i== 2 :
        mycar=Pickup(make,model)
        mycar.describe_vehicle()
        print (mycar.__dict__)
        x= input ("Do you want to try again? y/n: ")
        i = input ("Enter 1 for car, 2 for pickup and 3 for quit.")
        i = int(i)  
        if x == "n":
            break
       
        
    else :
        print ("please enter a valid number.")
        statues = False
print ("goooood bye!!!")
