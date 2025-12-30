# Lockr — Process Locking & Enforcement Tool

Lockr is a desktop application built in Python that allows users to monitor, lock, and actively enforce restrictions on running system processes. Once a process is locked, the application continuously prevents it from running until a specified expiration time.

---

## Running the Project

```bash
python main.py
```
### Prerequisites

- Python 3.9 or newer
- Required Python packages:
  - `psutil`
  - `customtkinter`

Install dependencies using:
```bash
pip install psutil customtkinter
```
---
## Features

### Live Process Table
- Displays currently running system processes  
- Automatically filters out OS-critical processes  
- Alphabetically sorted for clarity  

### Process Locking
- Lock any running process for a selectable duration  
- Locked processes are visually highlighted  
- Lock expiration time is tracked and displayed  

### Active Enforcement
- Background scheduler continuously checks for locked processes  
- Locked processes are automatically terminated if restarted  
- Processes unlock themselves when the lock expires  

### Responsive UI
- Built with `tkinter` and `ttk`  
- Alternating row colors for readability  
- Clear visual distinction between:
  - Running  
  - Selected  
  - Locked processes  

### Live Refresh
- Refreshes the process list while preserving locked processes  
- UI state is recalculated and repainted cleanly  

---

## Technologies Used

- **Python 3**
- **tkinter / ttk** — desktop UI
- **customtkinter** — desktop UI
- **psutil** — system process inspection and control
- **datetime** — lock expiration tracking
