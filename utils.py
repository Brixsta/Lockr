import psutil
import tkinter.messagebox as messagebox
from datetime import datetime, timedelta
import excluded
import Process

processes = {}

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
        selected_process_status_label.configure(text=f"{process.status} UNTIL: {process.lock_expiration}", text_color="red")

        # Turn locked rows red
        process_table.turn_locked_rows_red(process.name)

    else:
        print("YOU SAID NO")


# ----------------- Tick / Scheduler -----------------
def kill_locked():
    x = 1
    #
    # for pid in list(locked_processes):
    #
    #     try:
    #         psutil.Process(pid).kill()
    #         print(f"Killed process {pid}")
    #     except psutil.NoSuchProcess:
    #         print(f"Process {pid} does not exist!")
    #     except Exception as e:
    #         print(f"Unexpected Error killing process {pid}: {e}")


def tick(root):
    #kill_locked()
    root.after(1000, tick, root)
