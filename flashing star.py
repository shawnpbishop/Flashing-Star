from tkinter import *
from random import randint 

class FlashingStar:
    def __init__(self):
        window = Tk() 
        window.title("Flashing Star") 
        
        width = 300
        height = 300
        
        self.canvas = Canvas(window, width = width, height = height)
        self.canvas.pack()
        Button(window, text = "Display", command = self.display).pack()
        
        

        window.mainloop()

    def display(self):
        sleepTime = 100
        self.canvas.delete("star")
        colorList = ["red", "blue", "green", "yellow"]
        x = randint(0,3)
        verts = [10,40,40,40,50,10,60,40,90,40,65,60,75,90,50,70,25,90,35,60]
        for i in range(len(verts)):
            verts[i] += 100
        self.canvas.create_polygon(verts, fill=colorList[x], tags = "star")

        on = True
        while True:
            if on:
                self.canvas.create_polygon(verts, fill=colorList[x], tags = "star")
            else:
                self.canvas.delete("star")
                
            on = not on  
            self.canvas.after(sleepTime) # Sleep for 100 milliseconds
            self.canvas.update()
    
        

FlashingStar()
