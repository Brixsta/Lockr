from tkinter import ttk
import utils


class ProcessTable:
    def __init__(self, root, selected_process_name_label, selected_process_status_label):
        # Instantiate the Process Table
        self.root = root
        self.create_table()
        self.style_table()

        # Store values for each table row
        self.selected_row_id
        self.selected_pid
        self.selected_process_name
        self.selected_process_status

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

        # Loop through processes to fill table
        for key, values in utils.processes:
            self.treeview_table.insert("", "end", values=(key, values))

        # Bind select event to handle_select
        self.treeview_table.bind("<<TreeviewSelect>>", self.handle_select)

        # Grab the first row information when table is built
        first_row = self.treeview_table.get_children()[0]
        pid = self.treeview_table.item(first_row)['values'][0]
        process_name = self.treeview_table.item(first_row)['values'][1]

        # Update first row information
        self.selected_row_id = first_row
        self.selected_pid = pid
        self.selected_process_name = process_name
        self.selected_process_status = "RUNNING"

    def style_table(self):
        self.style_rows()
        self.style_headers()

    def style_rows(self):
        # Style rows

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
        self.treeview_table.tag_configure("ODD", background="white")
        self.treeview_table.tag_configure("EVEN", background="#EBF5FF")
        self.treeview_table.tag_configure("LOCKED", background="red")

        for index, item_id in enumerate(self.treeview_table.get_children()):
            if index % 2 == 0:
                tag = "EVEN"
            else:
                tag = "ODD"

            self.treeview_table.item(item_id, tags=(tag,))

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
        # Find values of selected row
        selected_row_id = event.widget.focus()
        item_values = event.widget.item(selected_row_id)['values']
        pid = item_values[0]
        process_name = item_values[1]
        tags = self.treeview_table.item(selected_row_id)['tags']
        status = ""

        if "EVEN" in tags or "ODD" in tags:
            status = "RUNNING"
        else:
            status = "LOCKED"

        # Store values of selected row
        self.selected_row_id = selected_row_id
        self.selected_pid = pid
        self.selected_process_name = process_name
        self.selected_process_status = status

        # Update selected_process_name_label
        self.selected_process_name_label.configure(text=f"Process Name: {process_name}")

        # Update selected_process_status_label
        self.selected_process_status_label.configure(text=f"{status}")

        # Change text color of selected_process_status_label
        if(status == "LOCKED"):
            self.selected_process_status_label.configure(text_color="red")
        else:
            self.selected_process_status_label.configure(text_color="green")
