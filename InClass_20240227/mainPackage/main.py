#main.py
# Add Import Statement for Vehicle class
from vehiclePackage.vehicleClass import *


if __name__ == "__main__":
    # Instantiate an object if type Vehicle
    myCorvette = Vehicle("Car", 120) # Trigger a call to constructor
    myCorvette.printType() #invoke the method on the object
    
    #Invoke the getter for maximum speed, store the return value in a variable
    #Print that to the console
    maximum_speed = myCorvette.getSpeed()
    print("Maximum speed:", maximum_speed)
    
    # instantiate another Vehicle object. You can name it
    myCorolla = Vehicle("Car") #myCorolla is an object of type Vehicle
    
    
    #I want a list of 3 Vehicles: Car, Boat, Space Ship
    # You can pick the names and properties
    # I want some friendly output to demonstrate your work
    myVehicles = [Vehicle("Toyota Camry",150), Vehicle("sailboat",20), Vehicle("Falcon Heavy",4000)]
# Iterate over the list
    for vehicle in myVehicles:
        vehicle.printType()
        print(vehicle.getSpeed())