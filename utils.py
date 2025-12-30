import psutil
import tkinter.messagebox as messagebox
from datetime import datetime
import GUI


# ----------------- Button toggle helpers -----------------

def toggle_lock_buttons(current_button, lock_buttons_list):
    # Set all buttons to up state
    for button in lock_buttons_list:
        button.configure(fg_color="#F0F0F0")

    # Set the button clicked to down state
    current_button.configure(fg_color="#DADADA")


def handle_confirm_lock_click(lock_buttons_list, process_table, selected_process_status_label):
    # Loop over lock buttons to see which has been pressed
    for button in lock_buttons_list:
        pressed = (button.cget("fg_color") == "#DADADA")
        if (pressed):
            # Grab time string
            lock_duration_str = button.cget("text")

            # Create prompt message
            create_lock_prompt(process_table, lock_duration_str, selected_process_status_label)


def handle_refresh_button_click(process_table, handle_search_bar_input):
    refresh_table(process_table, process_table.processes)
    handle_search_bar_input()


# ----------------- Message box helpers -----------------
def create_lock_prompt(process_table, lock_duration_str, selected_process_status_label):
    process = process_table.selected_process
    tree = process_table.treeview_table

    # Determine lock_duration_hours from lock_duration_str
    lock_duration_hours = int("".join(c for c in lock_duration_str if c.isdigit()))

    # Create prompt
    result = messagebox.askyesno(
        title="Confirm",
        message=f"Are you sure you want to lock {process.name} for {lock_duration_str}?"
    )

    # User presses "Yes"
    if result:
        name = process.name
        row_id = process_table.find_row_by_text(name)
        tree = process_table.treeview_table

        # Lock the process
        process.lock_process(lock_duration_hours)

        # Configure selected_process_status_label to red text with "LOCKED" message
        selected_process_status_label.configure(text=f"{process.status} UNTIL: {process.lock_expiration}",
                                                text_color="red")

    # User presses "No"
    else:
        pass


# ----------------- Tick / Scheduler -----------------
def tick(root, process_table):
    # Kill all locked processes
    kill_locked_processes(process_table)

    # Check locked processes to determine if they are still locked
    check_locked_processes_to_unlock(process_table)

    # Check selected_process_status_label
    check_selected_process_status_label(process_table)

    root.after(2000, tick, root, process_table)


def kill_locked_processes(process_table):
    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name']
            if name in process_table.names_of_locked_processes:
                proc.kill()
        # Exception to handle when the process is already deleted or access is denied by the Operating System
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass


def check_locked_processes_to_unlock(process_table):
    for name, process in process_table.processes.items():

        # Process is ready to be unlocked
        if process.status == "LOCKED" and datetime.now() >= process.expires_at:
            # Unlock process
            process.unlock_process()

            # Repaint the rows
            process_table.paint_alternating_rows()


def check_selected_process_status_label(process_table):
    curr = process_table.selected_process

    if curr.status == "RUNNING":
        process_table.selected_process_status_label.configure(text="RUNNING", text_color="green")

def refresh_table(process_table, processes):
    tree = process_table.treeview_table

    # Delete all current rows
    for item in tree.get_children():
        tree.delete(item)

    # Clear out unlocked processes
    process_table.clear_unlocked_processes()

    # Repopulate current processes, while including the locked processes
    process_table.populate_processes(tree)

    # Insert table rows check if they are locked
    for name in sorted(processes.keys(), key=str.lower):
        row_id = tree.insert(
            "",
            "end",
            values=(name,)
        )

    process_table.make_first_row_selected()
    process_table.paint_alternating_rows()