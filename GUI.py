import tkinter as tk
from tkinter import ttk
import ProcessTable
import utils
import customtkinter as ctk

# ------------------------- Constants ------------------------
FONT_TITLE = ("Helvetica", 22, "bold")
FONT_BUTTON = ("Helvetica", 16, "bold")
FONT_STATUS = ("Helvetica", 12, "bold")
BG_COLOR = "#EAEAEA"
BTN_BG = "#F0F0F0"
BTN_HOVER = "#DADADA"
BORDER_COLOR = "#C0C0C0"
TEXT_COLOR = "#1F2937"
# ------------------------------------------------------------

class GUI:
    def __init__(self, root):
        self.root = root
        self.build_ui()

    def build_ui(self):
        # Construct GUI
        self.configure_window()
        self.create_frames()
        self.configure_frames()
        self.create_widgets()

    def configure_window(self):
        # Specify window title
        self.root.title("Lockr")

        # Grab Screen Size
        screen_width = int(self.root.winfo_screenwidth() * .50)
        screen_height = int(self.root.winfo_screenheight() * .80)

        # Specify how big the window is
        self.root.geometry(f"{screen_width}x{screen_height}")

    def create_frames(self):
        # Create main_frame
        self.main_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.main_frame.pack(fill="both", expand=True)

        # Create left_main_frame
        self.left_main_frame = tk.Frame(self.main_frame, bg=BG_COLOR)
        self.left_main_frame.place(relx=0, rely=0, relwidth=.5, relheight=1)

        # Create search_bar_frame
        self.search_bar_frame = tk.Frame(self.left_main_frame, bg=BG_COLOR)
        self.search_bar_frame.pack(fill="x", padx=100, pady=(20, 0))

        # Create process_table_frame
        self.process_table_frame = tk.Frame(self.left_main_frame)
        self.process_table_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Create refresh_table_frame
        self.refresh_table_frame = tk.Frame(self.left_main_frame, bg=BG_COLOR)
        self.refresh_table_frame.pack(fill="x", padx=0, pady=(0, 20))

        # Create right_main_frame
        self.right_main_frame = tk.Frame(self.main_frame, bg=BG_COLOR)
        self.right_main_frame.place(relx=.5, rely=0, relwidth=.5, relheight=1)

        # Create lock_actions_frame
        self.lock_actions_frame = tk.Frame(self.right_main_frame, bg=BG_COLOR)
        self.lock_actions_frame.pack(fill="both", expand=True, padx=(0, 20), pady=20)

        # Create selected_process_frame
        self.selected_process_frame = tk.Frame(self.lock_actions_frame, bg=BG_COLOR)
        self.selected_process_frame.pack(fill="x", ipadx=10, ipady=10)

        # Create selected_process_status_frame
        self.selected_process_status_frame = tk.Frame(self.lock_actions_frame, bg=BG_COLOR)
        self.selected_process_status_frame.pack(fill="x")

        # Create lock_buttons_frame
        self.lock_buttons_frame = tk.Frame(self.lock_actions_frame, bg=BG_COLOR)
        self.lock_buttons_frame.pack(fill="x")

        # Create activate_lock_frame
        self.activate_lock_frame = tk.Frame(self.lock_actions_frame, bg=BG_COLOR)
        self.activate_lock_frame.pack(fill="x")

    def configure_frames(self):
        # Configure selected_process_frame
        self.selected_process_frame.rowconfigure(0, weight=1)
        self.selected_process_frame.rowconfigure(2, weight=1)
        self.selected_process_frame.columnconfigure(0, weight=1)
        self.selected_process_frame.columnconfigure(2, weight=1)

        # Configure lock_buttons_frame
        self.lock_buttons_frame.columnconfigure(0, weight=1)
        self.lock_buttons_frame.columnconfigure(6, weight=1)

        # Configure process_table_frame to accommodate the process_table and vsb
        self.process_table_frame.rowconfigure(0, weight=1)
        self.process_table_frame.columnconfigure(0, weight=1)
        self.process_table_frame.columnconfigure(1, weight=0)

    def create_widgets(self):
        self.create_labels()
        self.create_process_table()
        self.create_search_bar()
        self.create_buttons()

    def create_labels(self):
        # Create selected_process_status_label
        self.selected_process_status_label = ctk.CTkLabel(
            self.selected_process_status_frame,
            text="RUNNING",
            font=FONT_STATUS,
            text_color="Green",
        )
        self.selected_process_status_label.pack()

        # Create selected_process_name_label
        self.selected_process_name_label = ctk.CTkLabel(
            self.selected_process_frame,
            text=f"Process Name:",
            font=FONT_TITLE
        )
        self.selected_process_name_label.grid(column=1, row=1)

    def create_process_table(self):
        # Create process_table
        self.process_table = ProcessTable.ProcessTable(self.process_table_frame, self.selected_process_name_label,
                                                       self.selected_process_status_label)

        # Create vertical scrollbar
        vsb = ttk.Scrollbar(self.process_table_frame, orient="vertical",
                            command=self.process_table.treeview_table.yview)
        self.process_table.treeview_table.configure(yscrollcommand=vsb.set)
        self.process_table.treeview_table.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")

    def create_search_bar(self):
        # Create search_bar_entry
        self.search_var = ctk.StringVar()
        self.search_bar_entry = ctk.CTkEntry(self.search_bar_frame, placeholder_text="Enter process name here",
                                             font=("Helvetica", 14), border_width=1, border_color=BORDER_COLOR,
                                             text_color=TEXT_COLOR, textvariable=self.search_var)
        self.search_bar_entry.pack(fill="x", ipadx=10, ipady=5)
        self.search_var.trace_add("write", self.handle_search_bar_input)

    def create_buttons(self):
        # Create refresh_table_button
        self.refresh_table_button = ctk.CTkButton(self.refresh_table_frame,
                                                  text="Refresh Table",
                                                  text_color="white",
                                                  fg_color="forestgreen",
                                                  hover_color="#006400",
                                                  cursor="hand2",
                                                  font=FONT_BUTTON,
                                                  height=50,
                                                  command=lambda: utils.handle_refresh_button_click(self.process_table,
                                                                                                    self.handle_search_bar_input)
                                                  )
        self.refresh_table_button.pack(fill="x", padx=130)

        # Store lock_buttons in lock_button_list
        self.lock_buttons_list = []

        # Create one_hour_lock_button
        self.one_hour_lock_button = self.create_lock_button("1 Hour", BTN_HOVER, command=lambda: utils.toggle_lock_buttons(
            self.one_hour_lock_button, self.lock_buttons_list))
        self.one_hour_lock_button.pack(fill="x", pady=10)
        self.lock_buttons_list.append(self.one_hour_lock_button)

        # Create two_hour_lock_button
        self.two_hour_lock_button = self.create_lock_button("2 Hours", BTN_BG, command=lambda: utils.toggle_lock_buttons(
            self.two_hour_lock_button, self.lock_buttons_list))
        self.two_hour_lock_button.pack(fill="x", pady=10)
        self.lock_buttons_list.append(self.two_hour_lock_button)

        # Create three_hour_lock_button
        self.three_hour_lock_button = self.create_lock_button("3 Hours", BTN_BG, command=lambda: utils.toggle_lock_buttons(
            self.three_hour_lock_button, self.lock_buttons_list))
        self.three_hour_lock_button.pack(fill="x", pady=10)
        self.lock_buttons_list.append(self.three_hour_lock_button)

        # Create eight_hour_lock_button
        self.eight_hour_lock_button = self.create_lock_button("8 Hours", BTN_BG, command=lambda: utils.toggle_lock_buttons(
            self.eight_hour_lock_button, self.lock_buttons_list))
        self.eight_hour_lock_button.pack(fill="x", pady=10)
        self.lock_buttons_list.append(self.eight_hour_lock_button)

        # Create twentyfour_hour_lock_button
        self.twentyfour_hour_lock_button = self.create_lock_button("24 Hours", BTN_BG,
                                                                   command=lambda: utils.toggle_lock_buttons(
                                                                       self.twentyfour_hour_lock_button,
                                                                       self.lock_buttons_list))
        self.twentyfour_hour_lock_button.pack(fill="x", pady=10)
        self.lock_buttons_list.append(self.twentyfour_hour_lock_button)

        # Create confirm_lock_button
        self.confirm_lock_button = ctk.CTkButton(
            self.activate_lock_frame,
            text="Lock",
            font=FONT_BUTTON,
            height=50,
            corner_radius=8,
            cursor="hand2",
            text_color="white",
            fg_color="red",
            hover_color="#C00000",
            command=lambda: utils.handle_confirm_lock_click(self.lock_buttons_list, self.process_table,
                                                            self.selected_process_status_label)
        )
        self.confirm_lock_button.pack(fill="x", pady=10, padx=130)

    def handle_search_bar_input(self, *args):
        input_text = self.search_var.get().lower()
        table = self.process_table
        tree = table.treeview_table

        # Delete all current rows
        for item in tree.get_children():
            tree.delete(item)

        # Reinsert matching rows in alphabetical order
        for name in sorted(table.processes.keys(), key=str.lower):
            if name.lower().startswith(input_text):
                tree.insert("", "end", values=(name,))

        self.process_table.make_first_row_selected()

        # Paint the alternating row and locked effect
        table.paint_alternating_rows()

    def create_lock_button(self, text, fg_color, command):
        btn = ctk.CTkButton(
            self.lock_buttons_frame,
            text=text,
            text_color=TEXT_COLOR,
            fg_color=fg_color,
            hover_color=BTN_HOVER,
            border_width=1,
            border_color=BORDER_COLOR,
            cursor="hand2",
            font=FONT_BUTTON,
            height=50,
            command=command
        )
        return btn
