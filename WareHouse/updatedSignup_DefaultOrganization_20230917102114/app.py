'''
This file contains the App class that represents the authentication app GUI.
'''
import tkinter as tk
class App:
    def __init__(self, db):
        self.db = db
        self.window = tk.Tk()
        self.window.title("Authentication App")
        self.first_name_label = tk.Label(self.window, text="First Name:")
        self.first_name_label.pack()
        self.first_name_entry = tk.Entry(self.window)
        self.first_name_entry.pack()
        self.last_name_label = tk.Label(self.window, text="Last Name:")
        self.last_name_label.pack()
        self.last_name_entry = tk.Entry(self.window)
        self.last_name_entry.pack()
        self.email_label = tk.Label(self.window, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self.window)
        self.email_entry.pack()
        self.save_button = tk.Button(self.window, text="Save", command=self.save_user_info)
        self.save_button.pack()
    def save_user_info(self):
        '''
        This method is called when the "Save" button is clicked. It retrieves the user's input,
        saves the information into the database, and clears the input fields.
        '''
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        email = self.email_entry.get()
        self.db.save_user(first_name, last_name, email)
        self.first_name_entry.delete(0, tk.END)
        self.last_name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
    def run(self):
        '''
        This method starts the GUI event loop.
        '''
        self.window.mainloop()