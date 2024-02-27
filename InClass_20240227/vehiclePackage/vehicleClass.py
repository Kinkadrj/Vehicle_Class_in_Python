#vehicleClass.py

'''
Vehicle Class
This class models a vehicle on a used car lot
Change Order: we need to add maximum speed to the model.
Change Order: need a way to 'read' the maximum speed from the model
Change Order: Some developers need to use the constructor without having to provide a max speed
'''
# Constructor (Constructor is always __init__) we instantiate an object of Vehicle type
class Vehicle:
    def __init__(self, type, max_speed = None):
        '''
        @Param type: the kind of vehicle
        @Param max_speed: Maximum speed of the vehicle, defaults to None
        '''
        self.type = type;
        self._thisisprivate = 42 #This is a weak attempt to 'support' data hiding
        self.max_speed = max_speed # Save a copy in the current object
        
    # An instance method. It operates on an instance of a vehicle 
    def printType(self):
        print(self.type);
    
    def getSpeed(self):   # "a getter"
        return self.max_speed
            
if __name__ == "__main__":
    # Some code to test the class would go here.
    # If there's no code, just pass
    pass
