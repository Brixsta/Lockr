from tkinter import ttk
import utils


class ProcessTable:
    def __init__(self, root, process_selected_name):
        self.root = root
        self.process_selected_name = process_selected_name
        self.create_table()
        self.style_table()
        self.current_selected = [1, "undefined"]

    def create_table(self):
        # Create ptable
        self.ptable = ttk.Treeview(self.root, columns=["pid", "name"], show="headings")
        self.ptable.heading("pid", text="PID")
        self.ptable.heading("name", text="Process Name")
        self.ptable.pack(fill="both", expand=True)

        # Loop through processes to fill table
        for key, values in utils.processes:
            self.ptable.insert("", "end", values=(key, values))

        # Bind select event to handle_select
        self.ptable.bind("<<TreeviewSelect>>", self.handle_select)

        # Create ptable_style
        self.ptable_style = ttk.Style()

    def style_table(self):
        self.style_rows()
        self.style_headers()

    def style_rows(self):
        # Style rows
        self.ptable_style.configure(
            "Treeview",
            background="#F9FAFB",
            foreground="black",
            rowheight=28,
            fieldbackground="#F9FAFB",
            font=("Helvetica", 10)
        )

        # Set row colors
        self.ptable.tag_configure("odd", background="white")
        self.ptable.tag_configure("even", background="#EBF5FF")
        self.ptable.tag_configure("locked", background="red")

        for index, item_id in enumerate(self.ptable.get_children()):
            if index % 2 == 0:
                tag = "even"
            else:
                tag = "odd"

            self.ptable.item(item_id, tags=(tag,))

    def style_headers(self):
        # Create ptable_header_style
        self.ptable_header_style = ttk.Style()

        # Style table headers
        self.ptable_header_style.configure(
            "Treeview.Heading",
            background="#D0E4F7",  # header background color
            foreground="black",  # text color
            font=("Helvetica", 12),  # font and weight
            relief="raised"  # optional: 'flat', 'raised', 'sunken'
        )

        self.ptable_style.map(
            "Treeview.Heading",
            background=[("active", "#B0D4F1")]  # when hovering over header
        )

    def handle_select(self, event):
        selected_item = event.widget.focus()
        item_values = event.widget.item(selected_item)['values']
        pid = item_values[0]
        process_name = item_values[1]

        # Set current_selected pid and process_name
        self.set_current_selected(pid, process_name)

        # Change title on select
        self.process_selected_name.configure(text=f"Process Name: {process_name}")

    # ---------------------- Getters ------------------------

    def get_row_id_by_process_name(self, process_name):
        for item_id in self.ptable.get_children():
            values = self.ptable.item(item_id)['values']

            # print(f"values: {values[1]} process_name: {process_name}")

            if values and values[1] == process_name:
                return item_id

        return -1

    def get_current_selected(self):
        return self.current_selected

    def get_process_name(self):
        return self.current_selected[1]

    def get_pid(self):
        return self.current_selected[0]

    # ---------------------- Setters ------------------------

    def set_current_selected(self, pid, process_name):
        self.current_selected = [pid, process_name]
