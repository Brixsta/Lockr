import utils
from locked import locked_processes

class Process:
    def __init__(self, pid, name, status, lock_duration, treeview_table):
        self.pid = pid
        self.name = name
        self.status = status
        self.lock_duration = lock_duration
        self.lock_expiration = None
        self.treeview_table = treeview_table
        self.row_id = None

    def lock_process(self, lock_duration):
        self.status = "LOCKED"
        self.lock_duration = lock_duration

        # Calculate when lock expires
        expires_at = utils.compute_lock_expiration(lock_duration)
        self.lock_expiration = expires_at

    def unlock_process(self):
        self.status = "RUNNING"
        self.lock_duration = 0
        self.lock_expiration = None