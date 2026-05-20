import tkinter as tk
from tkinter import messagebox, ttk

class TodoApp:
    def __init__(self, root):
        # Initialize the main GUI window
        self.root = root
        self.root.title("Simple To-Do List")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Track tasks list and total count inside RAM
        self.tasks = []
        self.total_tasks_ever = 0
        
        # Create and display the main title
        title_label = tk.Label(root, text="My To-Do List", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Input field for typing new tasks
        self.task_entry = tk.Entry(root, font=("Arial", 12), width=25)
        self.task_entry.pack(pady=5)
        
        # Button to trigger adding a task
        add_btn = tk.Button(root, text="Add Task", font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", width=15, command=self.add_task)
        add_btn.pack(pady=5)
        
        # Graphical listbox to display all tasks on screen
        self.task_listbox = tk.Listbox(root, font=("Arial", 12), width=30, height=12)
        self.task_listbox.pack(pady=10)
        
        # Button to trigger removing a selected task
        remove_btn = tk.Button(root, text="Remove Completed", font=("Arial", 10, "bold"), bg="#f44336", fg="white", width=18, command=self.remove_task)
        remove_btn.pack(pady=5)
        
        # Text label to show percentage number
        self.progress_label = tk.Label(root, text="Progress: 0%", font=("Arial", 10, "bold"))
        self.progress_label.pack(pady=(10, 2))
        
        # Visual progress bar component
        self.progress_bar = ttk.Progressbar(root, orient="horizontal", length=280, mode="determinate")
        self.progress_bar.pack(pady=5)

    def add_task(self):
        # Get text from input box and remove extra spaces
        task = self.task_entry.get().strip()
        
        # If text is not empty, add it to list and update UI
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END) # Clear the input box
            self.total_tasks_ever += 1
            self.update_progress()
        else:
            # Show a pop-up warning if user clicks add without typing
            messagebox.showwarning("Warning", "Task field cannot be empty!")

    def remove_task(self):
        try:
            # Get the index of the selected item from listbox
            selected_index = self.task_listbox.curselection()[0]
            
            # Delete from both visual listbox and RAM list
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index)
            self.update_progress()
        except IndexError:
            # Show a pop-up warning if no task is selected to remove
            messagebox.showwarning("Warning", "Please select a completed task to remove.")

    def update_progress(self):
        # If there are no tasks, progress is 0%
        if self.total_tasks_ever == 0:
            percentage = 0
        else:
            # Calculate completion percentage based on removed tasks
            completed_tasks = self.total_tasks_ever - len(self.tasks)
            percentage = int((completed_tasks / self.total_tasks_ever) * 100)
        
        # Reset counters if all current tasks are cleared from the list
        if not self.tasks:
            percentage = 100 if self.total_tasks_ever > 0 else 0
            self.total_tasks_ever = 0
                
        # Apply changes to the visual progress bar and text label
        self.progress_bar['value'] = percentage
        self.progress_label.config(text=f"Progress: {percentage}%")

if __name__ == "__main__":
    # Main loop to keep the GUI window running
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()