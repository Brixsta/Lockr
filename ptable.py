from tkinter import ttk
import utils

class ProcessTable:
    def __init__(self, root, process_selected_name):
        self.root = root
        self.process_selected_name = process_selected_name
        self.create_table()
        self.current_selected = [1, "undefined"]

    def create_table(self):
        # Create my_table
        self.ptable = ttk.Treeview(self.root, columns=["pid", "name"], show="headings")
        self.ptable.heading("pid", text="PID")
        self.ptable.heading("name", text="Process Name")
        self.ptable.pack(fill="both", expand=True)

        # Loop through processes to fill table
        for key,values in utils.processes:
            self.ptable.insert("", "end", values=(key, values))

        # Bind select event to handle_select
        self.ptable.bind("<<TreeviewSelect>>", self.handle_select)

    def handle_select(self, event):
        selected_item = event.widget.focus()
        item_values = event.widget.item(selected_item)['values']
        pid = item_values[0]
        process_name = item_values[1]

        # Set current_selected pid and process_name
        self.set_current_selected(pid, process_name)

        # Change title on select
        self.process_selected_name.config(text=f"{process_name}")


    def get_current_selected(self):
        return self.current_selected

    def get_process_name(self):
        return self.current_selected[1]

    def get_pid(self):
        return self.current_selected[0]

    def set_current_selected(self, pid, process_name):
        self.current_selected = [pid, process_name]


