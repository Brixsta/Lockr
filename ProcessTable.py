from tkinter import ttk
import psutil
from Process import Process
import excluded


class ProcessTable:
    def __init__(self, root, selected_process_name_label, selected_process_status_label, ):
        self.root = root
        self.processes = {}
        self.names_of_locked_processes = set()

        # Handle the selected_process
        self.selected_process = None
        self.selected_process_name_label = selected_process_name_label
        self.selected_process_status_label = selected_process_status_label

        # Create and style treeview_table
        self.create_table()

        # Update selected_process_name_label intially
        selected_process_name_label.configure(
            text=f"Process Name: {self.selected_process.name}"
        )

    def populate_processes(self, treeview_table):
        # Gather processes excluding certain names
        for proc in psutil.process_iter(['pid', 'name']):
            if len(proc.info['name']) and proc.info['name'].lower() not in {name.lower() for name in excluded.OS}:
                # Gather attributes of the new_process
                name = proc.info['name']
                status = "RUNNING"
                lock_duration = 0
                new_process = Process(name, status, lock_duration, self.names_of_locked_processes, treeview_table)

                # Only add a process if it hasn't been seen before
                if name in self.processes:
                    continue
                else:
                    self.processes[name] = new_process

    def clear_unlocked_processes(self):
        for process_name, process in list(self.processes.items()):
            if process.name in self.names_of_locked_processes:
                continue
            else:
                del self.processes[process.name]

    def make_first_row_selected(self):
        # Grab first process after alphabetically sorting
        tree = self.treeview_table
        first_process_name = tree.item(tree.get_children()[0], "values")[0]
        row_id = self.find_row_by_text(first_process_name)
        process = self.processes[first_process_name]

        # Assign first process as the selected_process
        self.selected_process = process
        tree.item(row_id, tags=("SELECTED",))
        tree.selection_set(row_id)

        # Update text values of selected_process_name_label
        self.selected_process_name_label.configure(text=f"Process Name: {process.name}")

        # Update selected_process_status_label text
        self.selected_process_status_label.configure(text=f"{process.status}")

        # Update text color of selected_process_status_label
        if (process.status == "LOCKED"):
            self.selected_process_status_label.configure(text_color="red",
                                                         text=f"{process.status} UNTIL: {process.lock_expiration}")
        else:
            self.selected_process_status_label.configure(text_color="green")

    def create_table(self):
        # Create treeview_table
        self.treeview_table = ttk.Treeview(self.root, columns=["name"], show="headings")
        self.treeview_table.grid()
        self.treeview_table.heading("name", text="Process Name")

        # Generate treeview_table data
        self.populate_processes(self.treeview_table)

        # Insert table rows
        for name in sorted(self.processes.keys(), key=str.lower):
            self.treeview_table.insert(
                "",
                "end",
                values=(name,)
            )

        # Bind select event to handle_select
        self.treeview_table.bind("<<TreeviewSelect>>", self.handle_select)

        self.make_first_row_selected()

        # Apply table styling
        self.style_rows()
        self.style_headers()
        self.paint_alternating_rows()

    def style_rows(self):
        # Create treeview_table_style
        self.treeview_table_style = ttk.Style()

        # Style for row select effect
        self.treeview_table_style.map(
            "Treeview",
            background=[("selected", "#3B82F6")],  # background color
            foreground=[("selected", "white")]  # text color
        )

        # Style rows
        self.treeview_table_style.configure(
            "Treeview",
            foreground="black",
            rowheight=28,
            font=("Helvetica", 10),
            background="",
            fieldbackground=""
        )

        # Set row colors for running and locked
        self.treeview_table.tag_configure("SELECTED", background="#3B82F6", foreground="white")
        self.treeview_table.tag_configure("ODD", background="#F0F0F0")
        self.treeview_table.tag_configure("EVEN", background="#FFFFFF")
        self.treeview_table.tag_configure(
            "LOCKED",
            background="#FF0000"
        )

    def style_headers(self):
        # Style table headers
        self.treeview_table_style.configure(
            "Treeview.Heading",
            background="#D0E4F7",
            foreground="black",
            font=("Helvetica", 12),
            relief="raised"
        )

    def paint_alternating_rows(self):
        tree = self.treeview_table

        for index, row_id in enumerate(tree.get_children()):
            name = tree.item(row_id, "values")[0]
            process = self.processes[name]
            tag = "EVEN" if index % 2 == 0 else "ODD"
            selected_row = self.treeview_table.selection()[0]

            if process.status == "LOCKED":
                tree.item(row_id, tags=("LOCKED",))
            else:
                tree.item(row_id, tags=(tag,))

    def find_row_by_text(self, text):
        # Return treeview row id that's name value matches text
        for row_id in self.treeview_table.get_children():
            values = self.treeview_table.item(row_id, "values")
            row_text = values[0]

            if text == row_text:
                return row_id
        return None

    def handle_select(self, event):
        selected_row = event.widget.focus()
        if not selected_row:  # Nothing selected
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
            self.selected_process_status_label.configure(text_color="red",
                                                         text=f"{process.status} UNTIL: {process.lock_expiration}")
        else:
            self.selected_process_status_label.configure(text_color="green")
