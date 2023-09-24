'''
This is the main file of the application. It contains the GUI implementation and handles the remapping of keys.
'''
import tkinter as tk
import keyboard
class KeyRemapperApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Key Remapper")
        self.geometry("300x100")
        self.map_button = tk.Button(self, text="MapKeys", command=self.map_keys)
        self.map_button.pack(pady=10)
        self.reverse_button = tk.Button(self, text="ReverseKeys", command=self.reverse_keys)
        self.reverse_button.pack(pady=10)
    def map_keys(self):
        '''
        Remap the CAPSLOCK key to A and A key to CAPSLOCK
        '''
        keyboard.remap_key("capslock", "a")
        keyboard.remap_key("a", "capslock")
    def reverse_keys(self):
        '''
        Restore the original key mappings
        '''
        keyboard.remap_key("capslock", "capslock")
        keyboard.remap_key("a", "a")
if __name__ == "__main__":
    app = KeyRemapperApp()
    app.mainloop()