class Elevator:

  #default constructor method 
  
  def __init__(self, carID, currentFloor):
    self.carID = carID #int
    self.currentFloor = currentFloor #int 

    
  #function 1 : move elevator: this function will change the value of the current floor to the new floor
  def move(self, new_floor):
    self.currentFloor = new_floor

    
  def getCurrentFloor(self):
    return self.currentFloor 