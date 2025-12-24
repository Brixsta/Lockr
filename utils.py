import psutil
import tkinter.messagebox as messagebox
from datetime import datetime

# ----------------- Button toggle helpers -----------------
def toggle_processes(processes_button, websites_button):
    processes_button.configure(fg_color="#DADADA")
    websites_button.configure(fg_color="#F0F0F0")


def toggle_websites(processes_button, websites_button):
    processes_button.configure(fg_color="#F0F0F0")
    websites_button.configure(fg_color="#DADADA")


def toggle_lock_buttons(current_button, lock_buttons_list):
    # Set all buttons to up state
    for button in lock_buttons_list:
        button.configure(fg_color="#F0F0F0")

    # Set the button clicked to down state
    current_button.configure(fg_color="#DADADA")


def handle_confirm_lock_click(lock_buttons_list, process_table, selected_process_status_label):
    process = process_table.selected_process

    # Loop over lock buttons to see which has been pressed
    for button in lock_buttons_list:
        pressed = (button.cget("fg_color") == "#DADADA")
        if (pressed):
            # Grab time string
            lock_duration_str = button.cget("text")

            # Create prompt message
            create_lock_prompt(process_table, lock_duration_str, selected_process_status_label)


# ----------------- Message box helpers -----------------
def create_lock_prompt(process_table, lock_duration_str, selected_process_status_label):
    process = process_table.selected_process

    # Determine lock_duration_hours from lock_duration_str
    lock_duration_hours = int("".join(c for c in lock_duration_str if c.isdigit()))

    # Create prompt
    result = messagebox.askyesno(
        title="Confirm",
        message=f"Are you sure you want to lock {process.name} for {lock_duration_str}?"
    )

    # User presses "Yes"
    if result:
        # Lock the process
        process.lock_process(lock_duration_hours)

        # Configure selected_process_status_label to red text with "LOCKED" message
        selected_process_status_label.configure(text=f"{process.status} UNTIL: {process.lock_expiration}",
                                                text_color="red")

        # Turn locked rows red
        process_table.turn_locked_rows_red(process.name)

    else:
        print("YOU SAID NO")


# ----------------- Tick / Scheduler -----------------
def tick(root, process_table):
    # Kill all locked processes
    kill_locked_processes(process_table)

    # Repopulate processes to stay current
    process_table.populate_processes()

    # Check locked processes to determine if they are still locked
    check_locked_processes(process_table)

    root.after(2000, tick, root, process_table)


def kill_locked_processes(process_table):
    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name']
            if name in process_table.names_of_locked_processes:
                print(f"KILLING {name}")
                proc.kill()
        # Exception to handle when the process is already deleted or access is denied by the Operating System
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

def check_locked_processes(process_table):
    for name, process in process_table.processes.items():

        # Process is ready to be unlocked
        if process.status == "LOCKED" and datetime.now() >= process.expires_at:

            # Unlock process
            process.unlock_process()

            print(f"UNLOCKING {process.name}")

            # Determine row of the process to be unlocked
            process_table.turn_unlocked_rows_white(name)

            print(process.status)

