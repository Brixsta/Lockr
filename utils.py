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