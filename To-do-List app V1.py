import tkinter as tk
import sqlite3

conn = sqlite3.connect('tasks.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (task text)''')

def add_task():
    task = task_input.get()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    task_list.insert(tk.END, task)
    task_input.delete(0, tk.END)
    conn.commit()

def delete_task():
    task_to_delete = task_list.get(tk.ACTIVE)
    cursor.execute("DELETE FROM tasks WHERE task = (?)", (task_to_delete,))
    task_list.delete(tk.ACTIVE)
    conn.commit()

def mark_as_completed():
    selected_task = task_list.get(tk.ACTIVE)
    completed_list.insert(tk.END, selected_task)
    task_list.delete(tk.ACTIVE)

def edit_task():
    selected_task = task_list.get(tk.ACTIVE)
    task_input.delete(0, tk.END)
    task_input.insert(0, selected_task)
    task_list.delete(tk.ACTIVE)

root = tk.Tk()
root.title("To-Do List")

task_input = tk.Entry(root)
task_input.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

complete_button = tk.Button(root, text="Mark as Completed", command=mark_as_completed)
complete_button.pack()

edit_button = tk.Button(root, text="Edit Task", command=edit_task)
edit_button.pack()

task_list = tk.Listbox(root)
task_list.pack()

completed_list = tk.Listbox(root)
completed_list.pack()

# populate the task list from the database
cursor.execute("SELECT task FROM tasks")
tasks = cursor.fetchall()
for task in tasks:
    task_list.insert(tk.END, task[0])

root.mainloop()
