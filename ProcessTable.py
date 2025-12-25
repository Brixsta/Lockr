from tkinter import ttk
import psutil
from Process import Process
import excluded

class ProcessTable:
    def __init__(self, root, selected_process_name_label, selected_process_status_label, ):
        self.root = root
        self.processes = {}
        self.names_of_locked_processes = set()
        self.selected_process = None
        self.selected_process_name_label = selected_process_name_label
        self.selected_process_status_label = selected_process_status_label

        # Generate treeview_table data
        self.populate_processes()

        # Create and style treeview_table
        self.create_table()
        self.style_table()

    def populate_processes(self):
        # Gather processes excluding certain names
        for proc in psutil.process_iter(['pid', 'name']):
            if len(proc.info['name']) and proc.info['name'] not in excluded.OS:
                # Gather attributes of the new_process
                name = proc.info['name']
                status = "RUNNING"
                lock_duration = 0
                new_process = Process(name, status, lock_duration, self.names_of_locked_processes)

                if name in self.processes:
                    continue
                else:
                    self.processes[name] = new_process

    def clear_unlocked_processes(self):
        print(f"CURRENT LOCKED PROCESSES {self.names_of_locked_processes}")
        for process_name, process in list(self.processes.items()):
            if process.name in self.names_of_locked_processes:
                print(f"{process.name} is locked so I'm keeping it!")
                continue
            else:
                del self.processes[process.name]

        print(self.processes)


    def create_table(self):
        # Create treeview_table
        self.treeview_table = ttk.Treeview(self.root, columns=["name"], show="headings")
        self.treeview_table.grid()
        self.treeview_table.heading("name", text="Process Name")

        # Insert table rows with appropriate tags and sort them alphabetically
        for name in sorted(self.processes.keys(), key=str.lower):
            self.treeview_table.insert("", "end", values=(name,))

        # Add initial tags to processes so their colors alternate
        for index, row_id in enumerate(self.treeview_table.get_children()):
            name = self.treeview_table.item(row_id, "values")[0]
            process = self.processes[name]
            tag = "EVEN" if index % 2 == 0 else "ODD"
            process.tag = tag
            self.treeview_table.item(row_id, tags=(tag,))

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
            background="white",
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

        # Set row colors for running and locked
        self.treeview_table.tag_configure("LOCKED", background="red")
        self.treeview_table.tag_configure("ODD", background="#F0F0F0")
        self.treeview_table.tag_configure("EVEN", background="#FFFFFF")

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

    def find_row_by_text(self, text):
        # Return treeview row id that's name value matches text
        for row_id in self.treeview_table.get_children():
            values = self.treeview_table.item(row_id, "values")
            row_text = values[0]

            if text == row_text:
                return row_id
        return None

    def turn_locked_rows_red(self, text):
        row = self.find_row_by_text(text)
        row_text = self.treeview_table.item(row, "values")[0]

        # Turn row red by adding "LOCKED" tag
        if text == row_text:
            self.treeview_table.item(row, tags=("LOCKED",))

    def remove_red_rows(self, text):
        row = self.find_row_by_text(text)
        row_text = self.treeview_table.item(row, "values")[0]
        process = self.processes[row_text]

        # Turn row red by adding "LOCKED" tag
        if text == row_text:
            self.treeview_table.item(row, tags=(process.tag,))

    def handle_select(self, event):
        # Grab values for selected row and which process it belongs to
        selected_row = event.widget.focus()
        if not selected_row: # Nothing selected
            return

        item_values = event.widget.item(selected_row).get('values', [])
        if not item_values:  # Row has no values
            return

        name = item_values[0]
        process = self.processes[name]
        if not process:
            return

        # Update selected_process
        self.selected_process = process

        # Update text values of selected_process_name_label
        self.selected_process_name_label.configure(text=f"Process Name: {process.name}")

        # Update selected_process_status_label text
        self.selected_process_status_label.configure(text=f"{process.status}")

        # Update text color of selected_process_status_label
        if (process.status == "LOCKED"):
            self.selected_process_status_label.configure(text_color="red",text=f"{process.status} UNTIL: {process.lock_expiration}")
        else:
            self.selected_process_status_label.configure(text_color="green")