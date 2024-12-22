tasks = []

def main():
    first_run = True

    while True:
        if first_run:
            print("\nWelcome to stoaLists :)")
            first_run = False

        print("\nChoose an option: ")
        print("1. Add task")
        print("2. Delete task")
        print("3. Edit task")
        print("4. View task")
        print("5. Mark as completed")
        print("6. Exit")
        user_choice = input("Your choice: ")

        match user_choice:
            case "1":
                add_tasks()
            case "2":
                delete_tasks()
            case "3":
                edit_tasks()
            case "4":
                view_tasks()
            case "5":
                mark_tasks()
            case "6":
                print("\nGoodbye :)")
                break
            case _:
                print("Invalid choice")

def add_tasks():
    while True:
        try:
            task = input("\nEnter task (type exit to leave): ").strip().capitalize()

            if task.isdigit():
                print("Numbers are not allowed. Please enter a valid task.")
                continue

            if task == "Exit":
                break
            elif task not in tasks:
                tasks.append(task)
                print("Task added :)")
            else:
                print(f"{task} already exists in the to-do list.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

def delete_tasks():
    while True:
        if not tasks:
            print("\nNo tasks to delete.")
            break

        print("\nTasks:")
        for i, item in enumerate(tasks, start=1):
            print(f"{i}) {item}")

        delete_task = input("\nEnter task to delete (type 'exit' to leave): ").strip().capitalize()
        if delete_task == "Exit":
            break
        elif delete_task in tasks:
            tasks.remove(delete_task)
            print("Task deleted :)")
        else:
            print("Task not found. Please try again.")

def edit_tasks():
    while True:
        if not tasks:
            print("\nNo tasks to edit.")
            break

        print("\nTasks:")
        for i, item in enumerate(tasks, start=1):
            print(f"{i}) {item}")

        edit_task = input("\nEnter task to edit (type 'exit' to leave): ").strip().capitalize()
        if edit_task == "Exit":
            break
        elif edit_task in tasks:
            edited_task = input(f"What changes would you like to make to {edit_task}: ").strip().capitalize()
            if edited_task in tasks:
                print(f"The task '{edited_task}' already exists.")
            else:
                tasks[tasks.index(edit_task)] = edited_task
                print(f"The task '{edit_task}' has been updated to '{edited_task}'.")
        else:
            print("Task not found. Please try again.")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nTasks:")
        for i, item in enumerate(tasks, start=1):
            print(f"{i}) {item}")

def mark_tasks():
    while True:
        if not tasks:
            print("\nNo tasks to mark as completed.")
            break

        print("\nTasks:")
        for i, item in enumerate(tasks, start=1):
            print(f"{i}) {item}")

        mark_complete = input("What task would you like to mark as completed? (type exit to leave): ").strip().capitalize()

        if mark_complete == "Exit":
            break
        elif mark_complete in tasks:
            index = tasks.index(mark_complete)
            if "✓" in tasks[index]:
                print(f"'{mark_complete}' is already marked as completed.")
            else:
                tasks[index] = f"{tasks[index]} ✓"
                print(f"'{mark_complete}' has been marked as completed.")
        else:
            print("Task not found. Please try again.")


main()