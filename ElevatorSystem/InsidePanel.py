class InsidePanel: 
    def __init__(self):
        self.buttonList = [1,2,3,4,5]
        self.requestList = []

    def pressButton(self, button):
        self.requestList.append(button)
    
    
    def getFloorRequestList(self):
        return self.requestList
    
    def clearFloorRequestList(self):
        self.requestList = []
