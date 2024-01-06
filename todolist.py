def main():
    Tasks = []

    while True:
        print("\n == To Do List ==")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Mark a task as done")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            n_tasks = int(input("Enter how many tasks to add: "))
            for i in range(n_tasks):
                task = input("Enter the task: ")
                Tasks.append({"task": task, "done": False})
                print("Task added successfully!")

        elif choice == '2':
            print("\nTasks:")
            for index, task in enumerate(Tasks):
                status = "done" if task["done"] else "not done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: "))
            if 1 <= task_index <= len(Tasks):
                Tasks[task_index - 1]["done"] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")

        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
