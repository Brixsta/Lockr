import tkinter as tk
from ptable import ProcessTable
from tkinter import ttk

class LockrGUI:
    def __init__(self, root):
        self.root = root

        self.root.title("Lockr")
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

        # Create mode_buttons_frame
        self.mode_buttons_frame = tk.Frame(self.header_frame, bg="red")
        self.mode_buttons_frame.pack()

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

        # Create processes_container_frame
        self.processes_container_frame = tk.Frame(self.left_body_frame, bg="purple")
        self.processes_container_frame.place(relx=.5, rely=.5, relheight=.85, relwidth=.85, anchor="center")

        # Create right_body_frame
        self.right_body_frame = tk.Frame(self.body_frame, bg="black")
        self.right_body_frame.grid(column=1, row=0, sticky="nsew")

        # Configure right_body_frame
        self.right_body_frame.columnconfigure(0,weight=1)
        self.right_body_frame.rowconfigure(0, weight=0)

        # Create quick_lock_buttons_frame
        self.quick_lock_buttons_frame = tk.Frame(self.right_body_frame, bg="pink")
        self.quick_lock_buttons_frame.grid(column=0,row=2)

    def createWidgets(self):
        # Create app_button
        self.app_button = ttk.Button(self.mode_buttons_frame, text="Processes")
        self.app_button.grid(column=0, row=0)

        # Create web_button
        self.web_button = ttk.Button(self.mode_buttons_frame, text="Websites")
        self.web_button.grid(column=1, row=0)

        # Create lockr_title
        self.lockr_title = tk.Label(self.title_frame, text="Lockr")
        self.lockr_title.grid()

        # Create process_name_title
        self.process_name_title = tk.Label(self.right_body_frame, text="poop", bg="brown", width=10)
        self.process_name_title.grid(column=0, row=0, sticky="ew")

        # Create process_table
        self.process_table = ProcessTable(self.processes_container_frame, self.process_name_title)

        # Create lock_title
        self.lock_title = tk.Label(self.right_body_frame, text="Lock", bg="darkgrey", width=10)
        self.lock_title.grid(column=0,row=1, stick="ew")

        # Create lock_thirty_mins_button
        self.lock_thirty_mins_button = tk.Button(self.quick_lock_buttons_frame, text="30MIN")
        self.lock_thirty_mins_button.grid(column=0, row=0)

        # Create lock_one_hour_button
        self.lock_one_hour_button = tk.Button(self.quick_lock_buttons_frame, text="1H")
        self.lock_one_hour_button.grid(column=1, row=0)

        # Create lock_two_hour_button
        self.lock_two_hour_button = tk.Button(self.quick_lock_buttons_frame, text="2H")
        self.lock_two_hour_button.grid(column=2, row=0)

        # Create lock_four_hour_button
        self.lock_four_hour_button = tk.Button(self.quick_lock_buttons_frame, text="4H")
        self.lock_four_hour_button.grid(column=3, row=0)

        # Create lock_eight_hour_button
        self.lock_eight_hour_button = tk.Button(self.quick_lock_buttons_frame, text="8H")
        self.lock_eight_hour_button.grid(column=4, row=0)

        # Create lock_24_hour_button
        self.lock_24_hour_button = tk.Button(self.quick_lock_buttons_frame, text="24H")
        self.lock_24_hour_button.grid(column=5, row=0)

