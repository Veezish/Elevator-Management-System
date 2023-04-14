class Door:

    def __init__(self):
        self.state = False #initially door is always closed 
        self.timeToOpen = 5
        self.timeToClose = 5

    def openDoor(self):
        self.state = True 

    def closeDoor(self):
        self.state = False 
    
    # Did not use
    def getDoorStatus(self):
        return self.state
    
    # Did not use
    def setDoorStatus(self, input):
        self.state = input 