from tkinter import ttk
import utils


class ProcessTable:
    def __init__(self, root, selected_process_name_label, selected_process_status_label):
        self.root = root
        self.create_table()
        self.style_table()

        # Store values of table selected row
        self.selected_process = None

        # Label for the selected_process
        self.selected_process_name_label = selected_process_name_label

        # Label for the status of the selected_process
        self.selected_process_status_label = selected_process_status_label

    def create_table(self):
        # Create treeview_table
        self.treeview_table = ttk.Treeview(self.root, columns=["pid", "name"], show="headings")
        self.treeview_table.heading("pid", text="PID")
        self.treeview_table.heading("name", text="Process Name")
        self.treeview_table.pack(fill="both", expand=True)

        utils.get_running_processes(self.treeview_table)

        for pid, process in utils.processes.items():
            # Create the appropriate row
            utils.processes[pid].create_row()

        # Bind select event to handle_select
        self.treeview_table.bind("<<TreeviewSelect>>", self.handle_select)

    def style_table(self):
        self.style_rows()
        self.style_headers()

    def style_rows(self):
        # Create treeview_table_style
        self.treeview_table_style = ttk.Style()

        # Style rows
        self.treeview_table_style.configure(
            "Treeview",
            background="#F9FAFB",
            foreground="black",
            rowheight=28,
            fieldbackground="#F9FAFB",
            font=("Helvetica", 10)
        )

        # Create treeview_selected_row_style
        self.treeview_selected_row_style = ttk.Style()

        # Style selected rows
        self.treeview_selected_row_style.map(
            "Treeview",
            background=[("selected", "#0078D7")],  # color when row is selected
            foreground=[("selected", "white")]  # text color when selected
        )

        # Set row colors depending on tags
        self.treeview_table.tag_configure("RUNNING", background="white")
        self.treeview_table.tag_configure("LOCKED", background="red")


    def style_headers(self):
        # Create treeview_table_header_style
        self.treeview_table_header_style = ttk.Style()

        # Style table headers
        self.treeview_table_header_style.configure(
            "Treeview.Heading",
            background="#D0E4F7",
            foreground="black",
            font=("Helvetica", 12),
            relief="raised"
        )

    def handle_select(self, event):
        # Find values of selected process
        selected_row = event.widget.focus()
        item_values = event.widget.item(selected_row)['values']
        pid = item_values[0]
        process = utils.processes[pid]

        # Update selected_process
        self.selected_process = process

        # Update selected_process_name_label
        self.selected_process_name_label.configure(text=f"Process Name: {process.name}")

        # Update selected_process_status_label text
        self.selected_process_status_label.configure(text=f"{process.status}")

        # Update text color of selected_process_status_label
        if (process.status == "LOCKED"):
            self.selected_process_status_label.configure(text_color="red")
        else:
            self.selected_process_status_label.configure(text_color="green")
