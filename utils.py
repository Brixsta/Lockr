import psutil
from locked import locked_processes
import tkinter.messagebox as messagebox
from datetime import datetime, timedelta
import excluded
import Process

processes = {}

def populate_processes(table):
    # Gather processes excluding certain names
    for proc in psutil.process_iter(['pid', 'name']):
        if len(proc.info['name']) and proc.info['name'] not in excluded.OS:
            # Gather attributes of the new_process
            pid = proc.info['pid']
            name = proc.info['name']
            status = "RUNNING"
            lock_duration = 0
            new_process = Process.Process(pid, name, status, lock_duration, table)

            if name in processes:
                processes[name].append(new_process)
            else:
                processes[name] = [new_process]

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
            create_lock_prompt(process_table, process, lock_duration_str, selected_process_status_label)


# ----------------- Message box helpers -----------------
def create_lock_prompt(process_table, process, lock_duration_str, selected_process_status_label):

    # Determine lock_duration_hours from lock_duration_str
    lock_duration_hours = int("".join(c for c in lock_duration_str if c.isdigit()))

    # Create prompt
    result = messagebox.askyesno(
        title="Confirm",
        message=f"Are you sure you want to lock {process.name} for {lock_duration_str}?"
    )

    # User presses "Yes"
    if result:
        # Lock all the processes associated with that process name
        lock_processes_by_name(process.name, lock_duration_hours)

        # Configure selected_process_status_label to red text with "LOCKED" message
        selected_process_status_label.configure(text=f"{process.status} UNTIL: {process.lock_expiration}", text_color="red")

        # Turn locked rows red
        turn_locked_rows_red(process.name, process_table)

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

def compute_lock_expiration(lock_duration):
    now = datetime.now()
    expires_at = now + timedelta(hours=lock_duration)
    return expires_at.strftime("%b %d, %Y at %I:%M %p")

def lock_processes_by_name(name, lock_duration):
    for proc in processes[name]:
        proc.lock_process(lock_duration)

    for proc in processes[name]:
        print(f"{proc.status} {proc.pid}")

def turn_locked_rows_red(text, process_table):
    table = process_table.treeview_table
    row = find_row_by_text(text, table)
    row_text = table.item(row, "values")[0]

    # Turn row red by adding "LOCKED" tag
    if text == row_text:
        table.item(row, tags=("LOCKED",))

def find_row_by_text(text, table):
    # Loop through all row values
    for item_id in table.get_children():
        values = table.item(item_id, "values")
        row_text = values[0]

        if text == row_text:
            return item_id
    return -1