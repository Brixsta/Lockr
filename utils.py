import psutil

processes = []

for proc in psutil.process_iter(['pid', 'name']):
    if len(proc.info['name']):
        processes.append([proc.info['pid'], proc.info['name']])

def toggle_processes(button1, button2):
    button1.configure(fg_color="#DADADA")
    button2.configure(fg_color="#F0F0F0")

def toggle_websites(button1, button2):
    button2.configure(fg_color="#DADADA")
    button1.configure(fg_color="#F0F0F0")

def toggle_lock_buttons(current_button, lock_button_list):

    # Set all buttons to up state
    for button in lock_button_list:
        button.configure(fg_color = "#F0F0F0")

    # Set the button clicked to down state
    current_button.configure(fg_color = "#DADADA")


