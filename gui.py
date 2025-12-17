import tkinter as tk
import ptable
import utils
from tkinter import ttk
import customtkinter as ctk

class LockrGUI:
    def __init__(self, root):
        self.root = root

        self.root.title("Lockr")

        self.create_frames()
        self.configure_frames()
        self.create_widgets()

        # Grab Screen Size
        screen_width = int(root.winfo_screenwidth() * .50)
        screen_height = int(root.winfo_screenheight() * .80)

        # Specify how big the window is
        self.root.geometry(f"{screen_width}x{screen_height}")

    def create_frames (self):

        # Create header_frame
        self.header_frame = tk.Frame(self.root, bg="#EAEAEA")
        self.header_frame.pack(fill="x", ipady=10)

        # Create mode_buttons_frame
        self.mode_buttons_frame = tk.Frame(self.root, bg="#EAEAEA")
        self.mode_buttons_frame.pack(fill="x")

        # Create main_frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Create left_main_frame
        self.left_main_frame = tk.Frame(self.main_frame, bg="#EAEAEA")
        self.left_main_frame.place(relx=0, rely=0, relwidth=.5, relheight=1)

        # Create process_table_frame
        self.process_table_frame = tk.Frame(self.left_main_frame, bg="Orange")
        self.process_table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Create right_main_frame
        self.right_main_frame = tk.Frame(self.main_frame, bg="#EAEAEA")
        self.right_main_frame.place(relx=.5, rely=0, relwidth=.5, relheight=1)

        # Create lock_actions_frame
        self.lock_actions_frame = tk.Frame(self.right_main_frame, bg="#EAEAEA")
        self.lock_actions_frame.pack(fill="both", expand=True, padx=(0,20), pady=20)

        # Create process_selected_frame
        self.process_selected_frame = tk.Frame(self.lock_actions_frame,bg="#EAEAEA")
        self.process_selected_frame.pack(fill="x", ipadx=10, ipady=10)

        # Create lock_buttons_frame
        self.lock_buttons_frame = tk.Frame(self.lock_actions_frame, bg="#EAEAEA")
        self.lock_buttons_frame.pack(fill="x")

        # Create confirm_lock_frame
        self.confirm_lock_frame = tk.Frame(self.lock_actions_frame, bg="#EAEAEA")
        self.confirm_lock_frame.pack(fill="x")

    def configure_frames(self):
        # Configure mode_buttons_frame
        self.mode_buttons_frame.columnconfigure(0, weight=1)
        self.mode_buttons_frame.columnconfigure(3, weight=1)

        # Configure process_selected_frame
        self.process_selected_frame.rowconfigure(0, weight=1)
        self.process_selected_frame.rowconfigure(2, weight=1)
        self.process_selected_frame.columnconfigure(0, weight=1)
        self.process_selected_frame.columnconfigure(2, weight=1)

        # Configure lock_buttons_frame
        self.lock_buttons_frame.columnconfigure(0,weight=1)
        self.lock_buttons_frame.columnconfigure(6, weight=1)


    def create_widgets(self):

        # Create processes_button
        self.processes_button = ctk.CTkButton(
            self.mode_buttons_frame,
            text="Processes",
            text_color="#1F2937",
            fg_color="#DADADA",
            hover_color="#DADADA",
            border_width=1,
            border_color="#C0C0C0",
            cursor="hand2",
            font=("Helvetica", 14),
            command= lambda: utils.toggle_processes(self.processes_button, self.websites_button)
        )
        self.processes_button.grid(column=1, row=0, padx=10)

        # Create websites_button
        self.websites_button = ctk.CTkButton(
            self.mode_buttons_frame,
            text="Websites",
            text_color="#1F2937",
            fg_color="#F0F0F0",
            hover_color="#DADADA",
            border_width=1,
            border_color="#C0C0C0",
            cursor="hand2",
            font=("Helvetica", 14),
            command= lambda: utils.toggle_websites(self.processes_button, self.websites_button)
        )
        self.websites_button.grid(column=2, row=0, padx=10)

        # Create process_selected_name
        self.process_selected_name = ctk.CTkLabel(
            self.process_selected_frame,
            text="",
            font=("Helvetica", 18)
        )
        self.process_selected_name.grid(column=1, row=1)

        # Create process_table
        self.process_table = ptable.ProcessTable(self.process_table_frame, self.process_selected_name)

        # Create lock_buttons
        self.lock_duration = ctk.StringVar(value="30M")

        self.lock_buttons = ctk.CTkSegmentedButton(
            self.lock_buttons_frame,
            values=[" .5HR ", " 1HR ", " 2HR ", " 4HR ", " 8HR ", " Custom "],
            variable=self.lock_duration,
            fg_color="#EAEAEA",
            font=("Helvetica", 18, "bold"),
            text_color="#1F2937",
            unselected_color="#F0F0F0",
            unselected_hover_color="#DADADA",
            selected_hover_color="#DADADA",
            selected_color="#DADADA",
        )
        self.lock_buttons.pack()

        # Create confirm_lock_button
        self.confirm_lock_button = ctk.CTkButton(
            self.confirm_lock_frame,
            text="Lock",
            font=("Helvetica", 16, "bold"),
            height=44,
            corner_radius=8
        )
        self.confirm_lock_button.pack(pady=10)


