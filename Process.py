from datetime import datetime, timedelta


class Process:
    def __init__(self, name, status, lock_duration, names_of_locked_processes, treeview_table):
        self.name = name
        self.status = status
        self.lock_duration = lock_duration
        self.lock_expiration = None
        self.expires_at = None
        self.names_of_locked_processes = names_of_locked_processes
        self.treeview_table = treeview_table

    def lock_process(self, lock_duration):
        self.status = "LOCKED"
        self.lock_duration = timedelta(seconds=5)
        # self.lock_duration = lock_duration
        self.compute_lock_expiration()
        self.names_of_locked_processes.add(self.name)

        # Add tag to turn the locked row red
        row_id = self.find_row_id_of_process()
        self.treeview_table.item(row_id, tags=(self.status,))

    def unlock_process(self):
        self.status = "RUNNING"
        self.lock_duration = 0
        self.lock_expiration = None
        self.expires_at = None
        self.names_of_locked_processes.remove(self.name)


    def compute_lock_expiration(self):
        now = datetime.now()
        # self.expires_at = now + timedelta(self.lock_duration)
        self.expires_at = now + self.lock_duration
        self.lock_expiration = self.expires_at.strftime("%b %d, %Y at %I:%M %p")

    def find_row_id_of_process(self):
        tree = self.treeview_table

        for row_id in tree.get_children():
            values = tree.item(row_id, "values")
            name = values[0]
            if self.name == name:
                return row_id

        return None
