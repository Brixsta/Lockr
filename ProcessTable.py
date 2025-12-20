from tkinter import ttk
import utils


class ProcessTable:
    def __init__(self, root, selected_process_name_label):
        # Instantiate the Process Table
        self.root = root
        self.create_table()
        self.style_table()

        # Store values for each table row
        self.selected_row_id
        self.selected_pid
        self.selected_process_name

        # Label for the selected_process
        self.selected_process_name_label = selected_process_name_label

    def create_table(self):
        # Create process_table
        self.process_table = ttk.Treeview(self.root, columns=["pid", "name"], show="headings")
        self.process_table.heading("pid", text="PID")
        self.process_table.heading("name", text="Process Name")
        self.process_table.pack(fill="both", expand=True)

        # Loop through processes to fill table
        for key, values in utils.processes:
            self.process_table.insert("", "end", values=(key, values))

        # Bind select event to handle_select
        self.process_table.bind("<<TreeviewSelect>>", self.handle_select)

        # Grab the first row information when table is built
        first_row = self.process_table.get_children()[0]
        pid = self.process_table.item(first_row)['values'][0]
        process_name = self.process_table.item(first_row)['values'][1]

        # Update first row information
        self.selected_row_id = first_row
        self.selected_pid = pid
        self.selected_process_name = process_name

    def style_table(self):
        self.style_rows()
        self.style_headers()

    def style_rows(self):
        # Style rows

        # Create process_table_style
        self.process_table_style = ttk.Style()

        # Row styling
        self.process_table_style.configure(
            "Treeview",
            background="#F9FAFB",
            foreground="black",
            rowheight=28,
            fieldbackground="#F9FAFB",
            font=("Helvetica", 10)
        )

        # Set row colors
        self.process_table.tag_configure("odd", background="white")
        self.process_table.tag_configure("even", background="#EBF5FF")
        self.process_table.tag_configure("locked", background="red")

        for index, item_id in enumerate(self.process_table.get_children()):
            if index % 2 == 0:
                tag = "even"
            else:
                tag = "odd"

            self.process_table.item(item_id, tags=(tag,))

    def style_headers(self):
        # Create process_table_header_style
        self.process_table_header_style = ttk.Style()

        # Style table headers
        self.process_table_header_style.configure(
            "Treeview.Heading",
            background="#D0E4F7",  # header background color
            foreground="black",  # text color
            font=("Helvetica", 12),  # font and weight
            relief="raised"  # optional: 'flat', 'raised', 'sunken'
        )

        # Styles when hovering over the headers
        self.process_table_style.map(
            "Treeview.Heading",
            background=[("active", "#B0D4F1")]
        )

    def handle_select(self, event):
        # Find values of selected row
        selected_row_id = event.widget.focus()
        item_values = event.widget.item(selected_row_id)['values']
        pid = item_values[0]
        process_name = item_values[1]

        # Store values of selected row
        self.selected_row_id = selected_row_id
        self.selected_pid = pid
        self.selected_process_name = process_name

        # Update selected_process_name_label
        self.selected_process_name_label.configure(text=f"Process Name: {process_name}")