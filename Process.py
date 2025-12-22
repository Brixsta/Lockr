class Process:
    def __init__(self, pid, name, status, lock_duration, treeview_table):
        self.pid = pid
        self.name = name
        self.status = status
        self.lock_duration = lock_duration
        self.treeview_table = treeview_table
        self.row_id = None
        self.tag = "RUNNING"

    def lock_process(self, lock_duration):
        self.status = "LOCKED"
        self.lock_duration = lock_duration
        self.treeview_table.item(self.row_id, tags=(self.status,))

    def unlock_process(self):
        self.status = "RUNNING"
        self.lock_duration = 0
        self.treeview_table.item(self.row_id, tags=(self.status,))

    def create_row(self):
        self.row_id = self.treeview_table.insert("", "end", values=(self.pid, self.name), tags=(self.status,))