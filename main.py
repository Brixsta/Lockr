import tkinter as tk
from GUI import GUI
from utils import tick

root = tk.Tk()
app = GUI(root)

tick(root, app.process_table)  # continuous tick loop to check for active and locked processes

root.mainloop()