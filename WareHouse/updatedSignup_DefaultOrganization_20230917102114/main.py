'''
This is the main file that initializes the database and the app, and starts the GUI event loop.
'''
import tkinter as tk
from database import Database
from app import App
# Create an instance of the Database class
db = Database()
# Create an instance of the App class and pass the database instance
app = App(db)
# Start the GUI event loop
app.run()