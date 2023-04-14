import time 

class OutsidePanel:



    #constructor method 
    def __init__(self):

        self.button = ""
   


    # Did not use
    def is_button_pressed(self):
        if (self.button == ""):
            return False
        return True



    # Did not use
    def setButton(self, button):
        self.button = button

  
    def requestUp(self):
        self.button = "Up"

    
    def requestDown(self):
        self.button = "Down"
