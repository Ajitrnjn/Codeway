class ToDoListApp:
    def __init__(self):
        self.user_tasks = {}

    def add_task(self, username, task):
        if username not in self.user_tasks:
            self.user_tasks[username] = []

        self.user_tasks[username].append(task)
        print("Task added successfully!")

    def remove_task(self, username, index):
        if username in self.user_tasks:
            try:
                task = self.user_tasks[username].pop(index)
                print(f"Task '{task}' removed successfully!")
            except IndexError:
                print("Invalid task index!")
        else:
            print("User not found! Please log in.")

    def view_tasks(self, username):
        if username in self.user_tasks:
            tasks = self.user_tasks[username]
            if tasks:
                print("Your To-Do List:")
                for idx, task in enumerate(tasks, start=1):
                    print(f"{idx}. {task}")
            else:
                print("Your To-Do List is empty!")
        else:
            print("User not found! Please add user")

    def login(self, username):
        if username not in self.user_tasks:
            self.user_tasks[username] = []
            print(f"Welcome, {username}!")
        else:
            print(f"Welcome back, {username}!")

    def get_task_index(self, index_str):
        try:
            index = int(index_str)
            if index < 1:
                raise ValueError
            return index - 1
        except ValueError:
            print("Invalid task index!")
            return None
