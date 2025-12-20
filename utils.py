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


def handle_confirm_lock_click(lock_buttons_list, process_table):
    curr_selected_row = process_table.process_table.selection()
    process_name = process_table.selected_process_name
    process_time = ""
    lock_duration_hours = 0

    # Loop over buttons to see which has been pressed
    for button in lock_buttons_list:
        pressed = (button.cget("fg_color") == "#DADADA")
        if (pressed):
            # Grab time string
            process_time = button.cget("text")

            # Grab hour value
            lock_duration_hours = int("".join(c for c in process_time if c.isdigit()))

            # Create user prompt to confirm
            create_prompt(curr_selected_row, process_table, process_name, lock_duration_hours, f"Are you sure you want to lock {process_name} for {process_time}?")


# ----------------- Message box helpers -----------------
def create_prompt(curr_selected_row, process_table, process_name, lock_duration, prompt_message):
    result = messagebox.askyesno(
        title="Confirm",
        message=prompt_message
    )

    lock_amt = timedelta(hours=lock_duration)
    expires_at = datetime.now() + lock_amt

    if datetime.now() >= expires_at:
        print("unlocking")

    if result:
        locked.locked_processes[process_name] = expires_at
        highlight_locked_rows(curr_selected_row, process_table, process_name)


    else:
        print("YOU SAID NO")


# ----------------- Tick / Scheduler -----------------
def kill_locked():
    #print(f"Current Locked: {locked.locked_processes}")
    x = 1


def tick(root):
    kill_locked()
    root.after(1000, tick, root)

def highlight_locked_rows(curr_selected_row_id, process_table, process_name):
    process_table.process_table.item(curr_selected_row_id, tags=("locked",))

    print(f"process_name: {process_name} row id: {curr_selected_row_id}" )