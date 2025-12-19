import psutil
import excluded
import tkinter.messagebox as messagebox

processes = []

# Gather processes excluding certain names
for proc in psutil.process_iter(['pid', 'name']):
    if len(proc.info['name']) and proc.info['name'] not in excluded.OS:
        processes.append([proc.info['pid'], proc.info['name']])

# Dictionary to track locked processes
locked_processes = {

}

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
        button.configure(fg_color = "#F0F0F0")

    # Set the button clicked to down state
    current_button.configure(fg_color = "#DADADA")

def handle_confirm_lock_click(lock_buttons_list, process_selected_name):
    lock_text = (process_selected_name.cget("text"))[13:]
    process_time = ""
    lock_duration_hours = 0

    # Loop over buttons to see which has been pressed
    for button in lock_buttons_list:
        pressed = (button.cget("fg_color") == "#DADADA")
        if (pressed):
            # Grab time string
            process_time = button.cget("text")

            # Grab hour value
            lock_duration_hours= int("".join(c for c in process_time if c.isdigit()))

            # Create user prompt to confirm
            create_prompt(f"Are you sure you want to lock{lock_text} for {process_time}?")


# ----------------- Message box helpers -----------------
def create_prompt(prompt_message):
    result = messagebox.askyesno(
        title="Confirm",
        message=prompt_message
    )

# ----------------- Tick / Scheduler -----------------
def kill_locked():
    print("Finding the locked processes and killing them")

def tick(root):
    kill_locked()
    root.after(1000,tick, root)