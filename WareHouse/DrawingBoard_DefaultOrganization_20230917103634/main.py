'''
This is the main module that initializes the drawing board application.
'''
import tkinter as tk
from drawing_board import DrawingBoard
def main():
    root = tk.Tk()
    drawing_board = DrawingBoard(root)
    root.mainloop()
if __name__ == "__main__":
    main()