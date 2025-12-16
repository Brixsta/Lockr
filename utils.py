import psutil

processes = []

for proc in psutil.process_iter(['pid', 'name']):
    if len(proc.info['name']):
        processes.append([proc.info['pid'], proc.info['name']])