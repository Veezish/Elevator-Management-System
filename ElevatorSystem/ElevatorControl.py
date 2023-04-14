import InsidePanel 

class ElevatorControl:

    #global inside 
    #inside = InsidePanel.MyInsidePanel

    def __init__(self, insidePanel):
        self.queue = insidePanel.requestList
        
        
    def manageFloorRequestsUp(self):
        # Sorts floor request queue for elevator going up
        self.queue.sort()


    def manageFloorRequestsDown(self):
        # Sorts floor request queue for elevator going down
        self.queue.sort(reverse=True)

