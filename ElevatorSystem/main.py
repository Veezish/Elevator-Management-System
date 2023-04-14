import ElevatorControl
import Door
import Elevator
import OutsidePanel
import InsidePanel
import tkinter as tk
from PIL import ImageTk, Image

elevator = Elevator.Elevator(100, 1)  # Create elevator object
door = Door.Door()
outside_panel = OutsidePanel.OutsidePanel()
inside_panel = InsidePanel.InsidePanel()
elevator_control = ElevatorControl.ElevatorControl(inside_panel)



class UserInterface:
  def UserInterface():
    print("Hello World!")
    print("Welcome to the elevator system!")

   


   
  def on_click_up(self):
    outside_panel.requestUp()
    self.elevator_placement["image"] = self.test_opened_up
    self.direction_movement["text"] = "Going up, doors opening..." 

  def on_click_down(self):
    outside_panel.requestDown()
    self.elevator_placement["image"] = self.test_opened_down
    self.direction_movement["text"] = "Going down, doors opening..." 








  def update_queue_text(self): 
    self.queue_text["text"] = inside_panel.getFloorRequestList()

  def update_queue(self, floor_number):
    inside_panel.pressButton(floor_number)
    self.update_queue_text()





  def print_results(self):
    if outside_panel.button == "Up":
      elevator_control.manageFloorRequestsUp()
    else:
      elevator_control.manageFloorRequestsDown()


    list = inside_panel.getFloorRequestList()


    if outside_panel.button == "Up":
      for i in range(elevator.currentFloor, list[len(list) - 1] + 1):
        if i in inside_panel.requestList:
          self.passenger_activity.insert("1.0", "Passengers got off on floor " + str(i) + "\n")
      elevator.move(list[len(list) - 1])
     
    
    else:
      for i in range(elevator.currentFloor, list[len(list) - 1] - 2, -1):
        if i in inside_panel.requestList:
          self.passenger_activity.insert("1.0", "Passengers got off on floor " + str(i) + "\n")
      elevator.move(list[len(list) - 1] - 1)




  
    
    self.canvas.itemconfigure(self.canvas_text, text=str(elevator.currentFloor))
    self.elevator_placement["image"] = self.test_opened
    inside_panel.clearFloorRequestList()
    self.update_queue_text()
    self.direction_movement["text"] = "Currently on floor " + str(elevator.currentFloor) 








  
    

      
    


  



  def open_door(self):
      door.openDoor()
      self.elevator_placement["image"] = self.test_opened
      self.direction_movement["text"] = "Doors opening..." 

  def close_door(self):
    door.closeDoor()

    if outside_panel.button == "Up":
      self.elevator_placement["image"] = self.test_up
      
    elif outside_panel.button == "Down":
      self.elevator_placement["image"] = self.test_down
    else:
      self.elevator_placement["image"] = self.test_closed

    self.direction_movement["text"] = "Doors closing..." 





   



  def __init__(self):
    


    self.root = tk.Tk()
    self.root.geometry("900x620")
    self.root.minsize(900, 620)
    self.root.maxsize(900, 620)
    self.root.title("Elevator Management System")






    # GUI Title
    self.proj_title = tk.Label(self.root, text="Elevator Management System", font=('Arial', 18))
    self.proj_title.pack(padx=10,pady=10)

    self.canvas = tk.Canvas(self.root, width=20, height=20)
    self.canvas.pack(anchor='n')
    self.canvas_text = self.canvas.create_text(10, 10, text='', anchor=tk.NW, font=("Arial 9 bold"))
    self.canvas.itemconfigure(self.canvas_text, text=str(elevator.currentFloor))




    self.left_bar = tk.Frame(self.root, bg='lightgrey')
    self.left_bar.pack(side='left',  fill='both',  padx=5,  pady=5, expand=True)

    self.right_bar = tk.Frame(self.root, bg='lightgrey')
    self.right_bar.pack(side='right',  fill='both',  padx=5,  pady=5, expand=True)
   











    # Elevator images

    self.elevator_closed = Image.open("elevator_img/closed.png")
    self.elevator_down_button = Image.open("elevator_img/down_button.png")
    self.elevator_down = Image.open("elevator_img/down.png")
    self.elevator_opened = Image.open("elevator_img/opened.png")
    self.elevator_up_button = Image.open("elevator_img/up_button.png")
    self.elevator_up = Image.open("elevator_img/up.png")
    self.elevator_opened_up = Image.open("elevator_img/opened_up.png")
    self.elevator_opened_down = Image.open("elevator_img/opened_down.png")

    self.elevator_closed = self.elevator_closed.resize((233, 300), Image.ANTIALIAS)
    self.elevator_down_button = self.elevator_down_button.resize((233, 300), Image.ANTIALIAS)
    self.elevator_down = self.elevator_down.resize((233, 300), Image.ANTIALIAS)
    self.elevator_opened = self.elevator_opened.resize((233, 300), Image.ANTIALIAS)
    self.elevator_up_button = self.elevator_up_button.resize((233, 300), Image.ANTIALIAS)
    self.elevator_up = self.elevator_up.resize((233, 300), Image.ANTIALIAS)
    self.elevator_opened_up = self.elevator_opened_up.resize((233, 300), Image.ANTIALIAS)
    self.elevator_opened_down = self.elevator_opened_down.resize((233, 300), Image.ANTIALIAS)



    


    self.test_closed = ImageTk.PhotoImage(self.elevator_closed)
    self.test_down_button = ImageTk.PhotoImage(self.elevator_down_button)
    self.test_down = ImageTk.PhotoImage(self.elevator_down)
    self.test_opened = ImageTk.PhotoImage(self.elevator_opened)
    self.test_up_button = ImageTk.PhotoImage(self.elevator_up_button)
    self.test_up = ImageTk.PhotoImage(self.elevator_up)
    self.test_opened_up = ImageTk.PhotoImage(self.elevator_opened_up)
    self.test_opened_down = ImageTk.PhotoImage(self.elevator_opened_down)




    self.elevator_placement = tk.Label(image=self.test_closed)
    self.elevator_placement.pack()

    
    

    














    # Text that shows if elevator's moving up/down
    self.direction_movement = tk.Label(self.root, text="Currently on floor " + str(elevator.currentFloor), font=('Calibri 18 bold'))
    self.direction_movement.pack(anchor="s")








    # Displays elevator's current floor
    self.queue_title = tk.Label(self.root, 
                                  text="QUEUE", 
                                  font=('Calibri 12 bold'))
    self.queue_title.pack(fill='x')



    # Queue text
    self.queue_text = tk.Label(self.root,
                               text="",
                               font=('Arial, 10'))
    self.queue_text.pack()
    


































    self.outside_elevator_text = tk.Label(self.left_bar, text="Outside Elevator", font=('Arial, 18'), bg='lightgrey')
    self.outside_elevator_text.pack()




    

    self.up_button = tk.Button(self.left_bar, 
                            text="UP", 
                            font=('Arial, 10'), 
                            command=self.on_click_up,
                            height=1,
                            width=5)
    self.up_button.pack(pady=10)

    self.down_button = tk.Button(self.left_bar, 
                            text="DOWN", 
                            font=('Arial, 10'), 
                            command=self.on_click_down,
                            height=1,
                            width=5)
    self.down_button.pack(pady=10)



    self.elevator_control_text = tk.Label(self.left_bar, text="Elevator Control", font=('Arial, 18'), bg='lightgrey')
    self.elevator_control_text.pack()





    self.move_button = tk.Button(self.left_bar,
                                 text="MOVE ELEVATOR",
                                 font=('Arial, 10'),
                                 command = self.print_results,
                                 height=1,
                                 width=15)
    self.move_button.pack(pady=10)


    self.open_door_button = tk.Button(self.left_bar,
                                      text="OPEN DOORS",
                                      font=('Arial, 10'),
                                      command = self.open_door,
                                      height=1,
                                      width=12)
    self.open_door_button.pack(pady=10)

    self.close_door_button = tk.Button(self.left_bar,
                                      text="CLOSE DOORS",
                                      font=('Arial, 10'),
                                      command = self.close_door,
                                      height=1,
                                      width=12)
    self.close_door_button.pack(pady=10)







    # Inside Elevator buttons
    self.floors_text = tk.Label(self.right_bar, text="Inside Elevator", font=('Arial, 18'), bg='lightgrey')
    self.floors_text.pack(side='top')

    self.floor1_button = tk.Button(self.right_bar, 
                            text="1", 
                            font=('Arial, 10'), 
                            command= lambda: self.update_queue(1),
                            height=1,
                            width=5)
    self.floor1_button.pack(padx=0, pady=10)

    self.floor2_button = tk.Button(self.right_bar, 
                            text="2", 
                            font=('Arial, 10'), 
                            command= lambda: self.update_queue(2),
                            height=1,
                            width=5)
    self.floor2_button.pack(padx=0, pady=10)


    self.floor3_button = tk.Button(self.right_bar, 
                            text="3", 
                            font=('Arial, 10'), 
                            command= lambda: self.update_queue(3),
                            height=1,
                            width=5)
    self.floor3_button.pack(padx=0, pady=10)

    self.floor4_button = tk.Button(self.right_bar, 
                            text="4", 
                            font=('Arial, 10'), 
                            command= lambda: self.update_queue(4),
                            height=1,
                            width=5)
    self.floor4_button.pack(padx=0, pady=10)



    self.floor5_button = tk.Button(self.right_bar, 
                            text="5", 
                            font=('Arial, 10'), 
                            command= lambda: self.update_queue(5),
                            height=1,
                            width=5)
    self.floor5_button.pack(padx=0, pady=10)










    

    





    


    self.frame = tk.Frame(self.root, width=50, height=10)
    self.frame.pack(pady=10)

    # Text box for displaying passenger activity
    self.passenger_activity = tk.Text(self.frame, width=50, height=10, font=("Arial", 10))
    self.passenger_activity.pack()
    

    









   





    








    self.root.mainloop()
  





    
    


UserInterface()

