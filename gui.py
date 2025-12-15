import tkinter as tk
from tkinter import ttk

class LockrGUI:
    def __init__(self, root):
        self.root = root
        self.root.title = "Lockr"
        self.createFrames()
        self.createWidgets()

        # Grab Screen Size
        screen_width = int(root.winfo_screenwidth() * .50)
        screen_height = int(root.winfo_screenheight() * .80)

        # Specify how big the window is
        self.root.geometry(f"{screen_width}x{screen_height}")

    def createFrames (self):
        # Create title_frame
        self.title_frame = tk.Frame(self.root, bg="pink")
        self.title_frame.pack()

        # Create header_frame
        self.header_frame = tk.Frame(self.root, bg="blue")
        self.header_frame.pack(fill="x")

        # Create body_frame
        self.body_frame = tk.Frame(self.root, bg="green")
        self.body_frame.pack(fill="both", expand=True)

        # Configure body_frame
        self.body_frame.columnconfigure(0, weight=3)
        self.body_frame.columnconfigure(1, weight=2)
        self.body_frame.rowconfigure(0, weight=1)

        # Create left_body_frame
        self.left_body_frame = tk.Frame(self.body_frame, bg="orange")
        self.left_body_frame.grid(column=0, row=0, sticky="nsew")

        # Create table_container_frame
        self.table_container_frame = tk.Frame(self.left_body_frame, bg="purple")
        self.table_container_frame.place(relx=.5, rely=.5, relheight=.85, relwidth=.85, anchor="center")

        # Create right_body_frame
        self.right_body_frame = tk.Frame(self.body_frame, bg="black")
        self.right_body_frame.grid(column=1, row=0, sticky="nsew")

        # Create mode_buttons_frame
        self.mode_buttons_frame = tk.Frame(self.header_frame, bg="red")
        self.mode_buttons_frame.pack()

    def createWidgets(self):
        # Create app_button
        self.app_button = ttk.Button(self.mode_buttons_frame, text="App")
        self.app_button.grid(column=0, row=0)

        # Create web_button
        self.web_button = ttk.Button(self.mode_buttons_frame, text="Web")
        self.web_button.grid(column=1, row=0)

        # Create lockr_title
        self.lockr_title = tk.Label(self.title_frame, text="Lockr")
        self.lockr_title.grid()
