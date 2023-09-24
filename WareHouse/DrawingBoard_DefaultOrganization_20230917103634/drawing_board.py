'''
This module contains the DrawingBoard class that represents the drawing board application.
'''
import tkinter as tk
class DrawingBoard:
    def __init__(self, root):
        '''
        Initializes the DrawingBoard object.
        Parameters:
        - root: The root Tkinter object.
        Attributes:
        - root: The root Tkinter object.
        - canvas: The canvas widget for drawing.
        - color: The current drawing color.
        - cursor_size: The current cursor size.
        '''
        self.root = root
        self.root.title("Drawing Board")
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack()
        self.color = "black"
        self.cursor_size = 5
        self.canvas.bind("<B1-Motion>", self.draw)
        self.create_color_selector()
        self.create_cursor_size_selector()
    def draw(self, event):
        '''
        Draws a shape on the canvas.
        Parameters:
        - event: The mouse event.
        '''
        x, y = event.x, event.y
        self.canvas.create_oval(
            x - self.cursor_size,
            y - self.cursor_size,
            x + self.cursor_size,
            y + self.cursor_size,
            fill=self.color
        )
    def create_color_selector(self):
        '''
        Creates the color selector buttons.
        '''
        color_frame = tk.Frame(self.root)
        color_frame.pack(pady=10)
        color_frame.grid_columnconfigure(0, weight=1)
        colors = ["black", "red", "green", "blue", "yellow"]
        for color in colors:
            button = tk.Button(
                color_frame,
                bg=color,
                width=3,
                command=lambda c=color: self.set_color(c)
            )
            button.grid(row=0, column=colors.index(color), padx=5)
    def set_color(self, color):
        '''
        Sets the drawing color.
        Parameters:
        - color: The selected color.
        '''
        self.color = color
    def create_cursor_size_selector(self):
        '''
        Creates the cursor size selector buttons.
        '''
        size_frame = tk.Frame(self.root)
        size_frame.pack()
        sizes = [1, 3, 5, 7, 9]
        for size in sizes:
            button = tk.Button(
                size_frame,
                text=str(size),
                width=3,
                command=lambda s=size: self.set_cursor_size(s)
            )
            button.pack(side=tk.LEFT)
    def set_cursor_size(self, size):
        '''
        Sets the cursor size.
        Parameters:
        - size: The selected size.
        '''
        self.cursor_size = size
        self.canvas.config(cursor=f"circle {size}")