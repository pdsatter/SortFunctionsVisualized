from canvas import Canvas
import tkinter as tk

class TKCanvas(Canvas):
    def __init__(self, root, width, height):
        self.canvas = tk.Canvas(root, bg='white', width=width, height=height)

    def draw_circle(self, x, y, radius, outline="black", fill="blue"):
        return self.canvas.create_oval(x-radius, y-radius, x + radius, y + radius, 
                                       outline = outline, fill = fill,
                                       width = 2)
    
    def draw_square(self, x, y, width, outline="black", fill="blue"):
        return self.canvas.create_rectangle(x, y, x + 50, y + 50,
                                            outline = outline, fill = fill,
                                            width = 2)
    
    def draw_rectangle(self, x1, y1, x2, y2, outline="black", fill="blue"):
        return self.canvas.create_rectangle(x1, y1, x2, y2,
                                            outline = outline, fill = fill,
                                            width = 2)
                                            
    
    def draw_triangle(self, x, y, width, outline="black", fill="blue"):
        size = width
        points = [x - size, y, x + size, y, x, y - size]

        return self.canvas.create_polygon(points, 
                                          outline = outline, fill = fill,
                                          width = 2)
    
    def grid(self, row, column, columnspan):
        self.canvas.grid(row=row, column=column, columnspan=columnspan)

    def bind(self, button, function):
        self.canvas.bind(button, function)
    
    def delete(self, type):
        self.canvas.delete(type)

    def height(self):
        return int(self.canvas.winfo_reqheight())
    
    def width(self):
        return int(self.canvas.winfo_reqwidth())
    
    def update(self):
        self.canvas.update()