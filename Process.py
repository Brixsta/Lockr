from datetime import datetime, timedelta
import utils
from locked import locked_processes

class Process:
    def __init__(self, name, status, lock_duration):
        self.name = name
        self.status = status
        self.lock_duration = lock_duration
        self.lock_expiration = None

    def lock_process(self, lock_duration):
        self.status = "LOCKED"
        self.lock_duration = lock_duration
        self.compute_lock_expiration()

    def unlock_process(self):
        self.status = "RUNNING"
        self.lock_duration = 0
        self.lock_expiration = None

    def compute_lock_expiration(self):
        now = datetime.now()
        expires_at = now + timedelta(hours=self.lock_duration)
        self.lock_expiration = expires_at.strftime("%b %d, %Y at %I:%M %p")