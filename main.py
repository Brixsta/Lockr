import tkinter as tk
from GUI import GUI
from utils import tick

root = tk.Tk()
app = GUI(root)

tick(root, app.process_table)  # Start the ticking loop to check for locked processes

root.mainloop()