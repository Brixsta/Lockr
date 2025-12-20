import tkinter as tk
import ProcessTable
import utils
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

    def create_frames(self):
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
        self.lock_actions_frame.pack(fill="both", expand=True, padx=(0, 20), pady=20)

        # Create process_selected_frame
        self.process_selected_frame = tk.Frame(self.lock_actions_frame, bg="#EAEAEA")
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
        self.lock_buttons_frame.columnconfigure(0, weight=1)
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
            command=lambda: utils.toggle_processes(self.processes_button, self.websites_button)
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
            command=lambda: utils.toggle_websites(self.processes_button, self.websites_button)
        )
        self.websites_button.grid(column=2, row=0, padx=10)

        # Create selected_process_name_label
        first_process_name = utils.processes[0][1]
        self.selected_process_name_label = ctk.CTkLabel(
            self.process_selected_frame,
            text=f"Process Name: {first_process_name}",
            font=("Helvetica", 22, "bold")
        )
        self.selected_process_name_label.grid(column=1, row=1)

        # Create process_table
        self.process_table = ProcessTable.ProcessTable(self.process_table_frame, self.selected_process_name_label)

        # Store lock_buttons in lock_button_list
        self.lock_buttons_list = []

        # Create one_hour_lock_button
        self.one_hour_lock_button = ctk.CTkButton(
            self.lock_buttons_frame,
            text="1 Hour",
            text_color="#1F2937",
            fg_color="#DADADA",
            hover_color="#DADADA",
            border_width=1,
            border_color="#C0C0C0",
            cursor="hand2",
            font=("Helvetica", 16, "bold"),
            height=50,
            command=lambda: utils.toggle_lock_buttons(self.one_hour_lock_button, self.lock_buttons_list)
        )
        self.one_hour_lock_button.pack(fill="x", pady=10)
        self.lock_buttons_list.append(self.one_hour_lock_button)

        # Create two_hour_lock_button
        self.two_hour_lock_button = ctk.CTkButton(
            self.lock_buttons_frame,
            text="2 Hours",
            text_color="#1F2937",
            fg_color="#F0F0F0",
            hover_color="#DADADA",
            border_width=1,
            border_color="#C0C0C0",
            cursor="hand2",
            font=("Helvetica", 16, "bold"),
            height=50,
            command=lambda: utils.toggle_lock_buttons(self.two_hour_lock_button, self.lock_buttons_list)
        )
        self.two_hour_lock_button.pack(fill="x", pady=10)
        self.lock_buttons_list.append(self.two_hour_lock_button)

        # Create three_hour_lock_button
        self.four_hour_lock_button = ctk.CTkButton(
            self.lock_buttons_frame,
            text="4 Hours",
            text_color="#1F2937",
            fg_color="#F0F0F0",
            hover_color="#DADADA",
            border_width=1,
            border_color="#C0C0C0",
            cursor="hand2",
            font=("Helvetica", 16, "bold"),
            height=50,
            command=lambda: utils.toggle_lock_buttons(self.four_hour_lock_button, self.lock_buttons_list)
        )
        self.four_hour_lock_button.pack(fill="x", pady=10)
        self.lock_buttons_list.append(self.four_hour_lock_button)

        # Create eight_hour_lock_button
        self.eight_hour_lock_button = ctk.CTkButton(
            self.lock_buttons_frame,
            text="8 Hours",
            text_color="#1F2937",
            fg_color="#F0F0F0",
            hover_color="#DADADA",
            border_width=1,
            border_color="#C0C0C0",
            cursor="hand2",
            font=("Helvetica", 16, "bold"),
            height=50,
            command=lambda: utils.toggle_lock_buttons(self.eight_hour_lock_button, self.lock_buttons_list)
        )
        self.eight_hour_lock_button.pack(fill="x", pady=10)
        self.lock_buttons_list.append(self.eight_hour_lock_button)

        # Create custom_lock_button
        self.twentyfour_hour_lock_button = ctk.CTkButton(
            self.lock_buttons_frame,
            text="24 Hours",
            text_color="#1F2937",
            fg_color="#F0F0F0",
            hover_color="#DADADA",
            border_width=1,
            border_color="#C0C0C0",
            cursor="hand2",
            font=("Helvetica", 16, "bold"),
            height=50,
            command=lambda: utils.toggle_lock_buttons(self.twentyfour_hour_lock_button, self.lock_buttons_list)
        )
        self.twentyfour_hour_lock_button.pack(fill="x", pady=10)
        self.lock_buttons_list.append(self.twentyfour_hour_lock_button)

        # Create confirm_lock_button
        self.confirm_lock_button = ctk.CTkButton(
            self.confirm_lock_frame,
            text="Lock",
            font=("Helvetica", 16, "bold"),
            height=44,
            corner_radius=8,
            cursor="hand2",
            text_color="white",
            fg_color="red",
            hover_color="red",
            command=lambda: utils.handle_confirm_lock_click(self.lock_buttons_list, self.process_table)
        )
        self.confirm_lock_button.pack(pady=10)
