import psutil
import excluded
import tkinter.messagebox as messagebox

processes = []

for proc in psutil.process_iter(['pid', 'name']):
    if len(proc.info['name']) and proc.info['name'] not in excluded.windows and proc.info['name'] not in excluded.mac:
        processes.append([proc.info['pid'], proc.info['name']])

def toggle_processes(button1, button2):
    button1.configure(fg_color="#DADADA")
    button2.configure(fg_color="#F0F0F0")

def toggle_websites(button1, button2):
    button2.configure(fg_color="#DADADA")
    button1.configure(fg_color="#F0F0F0")

def toggle_lock_buttons(current_button, lock_buttons_list):

    # Set all buttons to up state
    for button in lock_buttons_list:
        button.configure(fg_color = "#F0F0F0")

    # Set the button clicked to down state
    current_button.configure(fg_color = "#DADADA")

def handle_confirm_lock_click(lock_buttons_list, process_selected_name):
    process_name = process_selected_name.cget("text")
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
            create_prompt(f"Are you sure you want to lock{process_name[13:]} for {process_time}?")

def create_prompt(prompt_message):
    result = messagebox.askyesno(
        title="Confirm",
        message=prompt_message
    )



