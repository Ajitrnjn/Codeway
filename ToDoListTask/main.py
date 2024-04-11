from task import Task
from to_do_list import ToDoListApp


def main():
    todo_app = ToDoListApp()

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            task_description = input("Enter task description: ")
            task = Task(task_description)
            todo_app.add_task(username, task)
        elif choice == '2':
            username = input("Enter your username: ")
            index_str = input("Enter task index to remove: ")
            index = todo_app.get_task_index(index_str)
            if index is not None:
                todo_app.remove_task(username, index)
        elif choice == '3':
            username = input("Enter your username: ")
            todo_app.view_tasks(username)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
