import psutil
import locked
import tkinter.messagebox as messagebox
from datetime import datetime, timedelta
import excluded

processes = []

# Gather processes excluding certain names
for proc in psutil.process_iter(['pid', 'name']):
    if len(proc.info['name']) and proc.info['name'] not in excluded.OS:
        processes.append([proc.info['pid'], proc.info['name']])


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
    selected_row_id = process_table.selected_row_id
    process_name = process_table.selected_process_name
    process_time = ""
    lock_duration = 0

    # Loop over buttons to see which has been pressed
    for button in lock_buttons_list:
        pressed = (button.cget("fg_color") == "#DADADA")
        if (pressed):
            # Grab time string
            process_time = button.cget("text")

            # Grab hour value
            lock_duration = int("".join(c for c in process_time if c.isdigit()))

            # Create user prompt to confirm
            create_prompt(lock_duration, process_table,
                          f"Are you sure you want to lock {process_name} for {process_time}?")


# ----------------- Message box helpers -----------------
def create_prompt(lock_duration, process_table, prompt_message):
    result = messagebox.askyesno(
        title="Confirm",
        message=prompt_message
    )

    # User presses "Yes" on Prompt
    if result:
        lock_process(process_table, lock_duration)

    else:
        print("YOU SAID NO")


# ----------------- Tick / Scheduler -----------------
def kill_locked():
    # print(f"Current Locked: {locked.locked_processes}")
    x = 1


def tick(root):
    kill_locked()
    root.after(1000, tick, root)


def lock_process(process_table, lock_duration):
    # Add process to locked processes dict [pid] = lock_expiration
    pid = process_table.selected_pid
    lock_expiration = compute_lock_expiration(lock_duration)
    locked.processes[pid] = lock_expiration

    # Visually update UI to reflect locked process state
    style_locked_process(process_table)

    # Change process status to locked
    process_table.selected_process_status = "LOCKED"


def style_locked_process(process_table):
    pid = process_table.selected_pid

    # Find lock expiration
    lock_expiration = find_locked_process_by_pid(pid)

    # Change selected_process_status_label text
    process_table.selected_process_status_label.configure(text=f"LOCKED {lock_expiration}")

    # Turn selected_process_status_label text to red
    process_table.selected_process_status_label.configure(text_color="red")

    # Change locked rows to red
    process_table.treeview_table.item(process_table.selected_row_id, tags=("LOCKED",))


def compute_lock_expiration(lock_duration):
    now = datetime.now()
    expires_at = now + timedelta(hours=lock_duration)
    return expires_at

def find_locked_process_by_pid(process_pid):
    for pid, lock_expiration in locked.processes.items():
        if process_pid == pid:
            return locked.processes[pid]
    return -1