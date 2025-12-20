import tkinter as tk
from GUI import GUI
import utils

root = tk.Tk()
app = GUI(root)

utils.tick(root)  # Start the ticking loop to check for locked processes

root.mainloop()