def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def task():
    tasks = load_tasks()
    print("\n----- WELCOME TO THE TASK MANAGEMENT APP -----")

    while True:
        print("\nChoose an option:")
        print("1. Add Task(s)")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")

        try:
            operation = int(input("Enter choice (1–5): "))
        except ValueError:
            print("Kindly enter a number between 1 and 5.")
            continue
        
        if operation == 1:
            try:
                count = int(input("How many tasks do you want to add? "))
                for i in range(1, count + 1):
                    new_task = input(f"Enter task {i}: ").strip()
                    if new_task:
                        tasks.append(new_task)
                    else:
                        print("Empty task skipped.")
                save_tasks(tasks)
                print(f"{count} task(s) added successfully.")
            except ValueError:
                print("Please enter a valid number.")

        elif operation == 2:
            if not tasks:
                print("No tasks to update.")
                continue

            print("\nYour To-Do List:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

            updated_val = input("Enter the task name you want to update: ").strip()
            if updated_val in tasks:
                updated = input("Enter new task: ").strip()
                if updated:
                    index = tasks.index(updated_val)
                    tasks[index] = updated
                    save_tasks(tasks)
                    print(f"Task '{updated_val}' has been updated to '{updated}'.")
                else:
                    print("New task cannot be empty.")
            else:
                print(f"Task '{updated_val}' not found.")

        elif operation == 3:
            if not tasks:
                print("No tasks to delete.")
                continue

            print("\nYour To-Do List:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t}")

            deleted_val = input("Enter the task name you want to delete: ").strip()
            if deleted_val in tasks:
                tasks.remove(deleted_val)
                save_tasks(tasks)
                print(f"Task '{deleted_val}' has been deleted.")
            else:
                print(f"Task '{deleted_val}' not found.")

        elif operation == 4:
            if not tasks:
                print("No tasks in your list.")
            else:
                print("\nYour To-Do List:")
                for i, t in enumerate(tasks, 1):
                    print(f"{i}. {t}")

        elif operation == 5:
            print("Closing the Task Manager. Goodbye!")
            break

        else:
            print("Invalid input. Please select a number from 1 to 5.")


task()
