import tkinter as tk
from tkinter import messagebox

# Create main window
root = tk.Tk()
root.title("Simple To-Do List")
root.geometry("400x450")
root.resizable(False, False)

# ----- Functions -----

def add_task():
    task = task_entry.get().strip()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def delete_all_tasks():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?"):
        task_listbox.delete(0, tk.END)

# ----- UI Components -----

title_label = tk.Label(root, text="To-Do List", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=30, font=("Arial", 12))
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=35, height=12, font=("Arial", 12))
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Selected Task", width=20, command=delete_task)
delete_button.pack(pady=5)

delete_all_button = tk.Button(root, text="Delete All Tasks", width=20, command=delete_all_tasks)
delete_all_button.pack(pady=5)

# Run the application
root.mainloop()
