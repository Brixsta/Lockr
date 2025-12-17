import tkinter as tk
from ptable import ProcessTable
from tkinter import ttk

class LockrGUI:
    def __init__(self, root):
        self.root = root

        self.root.title("Lockr")

        self.create_frames()
        self.configure_frames()
        self.create_widgets()
        self.style_widgets()

        # Grab Screen Size
        screen_width = int(root.winfo_screenwidth() * .50)
        screen_height = int(root.winfo_screenheight() * .80)

        # Specify how big the window is
        self.root.geometry(f"{screen_width}x{screen_height}")

    def create_frames (self):
        # Create header_frame
        self.header_frame = tk.Frame(self.root, bg="#EAEAEA")
        self.header_frame.pack(fill="x")

        # Create mode_buttons_frame
        self.mode_buttons_frame = tk.Frame(self.root, bg="#EAEAEA")
        self.mode_buttons_frame.pack(fill="x")

        # Create main_frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Create left_main_frame
        self.left_main_frame = tk.Frame(self.main_frame, bg="orange", padx=20, pady=20)
        self.left_main_frame.place(relx=0, rely=0, relwidth=.5, relheight=1)

        # Create right_main_frame
        self.right_main_frame = tk.Frame(self.main_frame, bg="blue")
        self.right_main_frame.place(relx=.5, rely=0, relwidth=.5, relheight=1)

        # Create process_selected_frame
        self.process_selected_frame = tk.Frame(self.right_main_frame)
        self.process_selected_frame.pack(fill="x")

        # Create lock_buttons_frame
        self.lock_buttons_frame = tk.Frame(self.right_main_frame, bg="brown")
        self.lock_buttons_frame.pack(fill="both", expand=True)

    def configure_frames(self):
        # Configure mode_buttons_frame
        self.mode_buttons_frame.columnconfigure(0, weight=1)
        self.mode_buttons_frame.columnconfigure(3, weight=1)

        #Configure lock_buttons_frame
        self.lock_buttons_frame.columnconfigure(0,weight=1)
        self.lock_buttons_frame.columnconfigure(6, weight=1)


    def create_widgets(self):
        # Create lockr_title
        self.lockr_title = ttk.Label(self.header_frame, text="Lockr", style="lockr_title_style.TLabel")
        self.lockr_title.pack()

        # Create processes_button
        self.processes_button = ttk.Button(self.mode_buttons_frame, text="Processes", style="mode_button_style.TButton")
        self.processes_button.grid(column=1, row=0, pady=0, padx=10)

        # Create websites_button
        self.websites_button = ttk.Button(self.mode_buttons_frame, text="Websites", style="mode_button_style.TButton")
        self.websites_button.grid(column=2, row=0, pady=0, padx=10)

        # Create process_selected_name
        self.process_selected_name = ttk.Label(self.process_selected_frame, text="", anchor="center", style="process_selected_name.TLabel")
        self.process_selected_name.pack(fill="x")

        # Create process_table
        self.process_table = ProcessTable(self.left_main_frame, self.process_selected_name)

        # Create lock_30_button
        self.lock_30_button = ttk.Button(self.lock_buttons_frame, text="30M", style="lock_buttons_style.TButton", width=5)
        self.lock_30_button.grid(column=1, row=0, padx=5)

        # Create lock_1_button
        self.lock_1_button = ttk.Button(self.lock_buttons_frame, text="1H", style="lock_buttons_style.TButton", width=5)
        self.lock_1_button.grid(column=2, row=0, padx=5)

        # Create lock_2_button
        self.lock_2_button = ttk.Button(self.lock_buttons_frame, text="2H", style="lock_buttons_style.TButton", width=5)
        self.lock_2_button.grid(column=3, row=0, padx=5)

        # Create lock_4_button
        self.lock_4_button = ttk.Button(self.lock_buttons_frame, text="4H", style="lock_buttons_style.TButton", width=5)
        self.lock_4_button.grid(column=4, row=0, padx=5)

        # Create lock_8_button
        self.lock_8_button = ttk.Button(self.lock_buttons_frame, text="8H", style="lock_buttons_style.TButton", width=5)
        self.lock_8_button.grid(column=5, row=0, padx=5)


    def style_widgets(self):

        # Style lockr_title
        self.lockr_title_style = ttk.Style()
        self.lockr_title_style.configure(
            "lockr_title_style.TLabel",
            foreground="#111111",
            background="#EAEAEA",
            font=("Helvetica", 16),
            padding=10
        )

        # Style mode_buttons
        self.mode_buttons_style = ttk.Style()
        self.mode_buttons_style.configure(
            "mode_button_style.TButton",
            font=("Helvetica", 12),
            padding=5
        )

        # Style process_selected_name
        self.process_selected_name_style = ttk.Style()
        self.process_selected_name_style.configure(
            "process_selected_name.TLabel",
            foreground="#111111",
            #background="#EAEAEA",
            background="pink",
            font=("Helvetica", 16),
            padding=10
        )

        # Style lock_buttons
        self.lock_buttons_style = ttk.Style()
        self.lock_buttons_style.configure(
            "lock_buttons_style.TButton",
            font=("Helvetica", 16, "bold")
        )


