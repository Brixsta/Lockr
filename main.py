import tkinter as tk
from gui import LockrGUI
import utils

root = tk.Tk()
app = LockrGUI(root)

utils.tick(root) # Start the ticking loop to check for locked processes

root.mainloop()

