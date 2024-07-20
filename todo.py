def task_manager():
    tasks = []  # Initialize an empty list to store tasks
    print("==== Welcome to Your Personal Task Manager ====")
    
    try:
        total_tasks = int(input("How many tasks would you like to add initially? "))
    except ValueError:
        print("Please enter a valid number.")
        return
    
    for i in range(total_tasks):
        task_name = input(f"Enter the name of task {i + 1}: ")
        tasks.append(task_name)
    
    print("\nToday's tasks are:")
    for task in tasks:
        print(f"- {task}")
    
    while True:
        print("\nOptions:")
        print("1 - Add a task")
        print("2 - Update a task")
        print("3 - Delete a task")
        print("4 - View all tasks")
        print("5 - Exit the program")
        
        try:
            choice = int(input("Choose an option by entering the corresponding number: "))
            
            if choice == 1:
                new_task = input("Enter the name of the task you want to add: ")
                tasks.append(new_task)
                print(f"Task '{new_task}' added successfully.")
            
            elif choice == 2:
                task_to_update = input("Enter the name of the task you want to update: ")
                if task_to_update in tasks:
                    new_name = input("Enter the new name for the task: ")
                    index = tasks.index(task_to_update)
                    tasks[index] = new_name
                    print(f"Task '{task_to_update}' updated to '{new_name}'.")
                else:
                    print("Task not found. Please try again.")
            
            elif choice == 3:
                task_to_delete = input("Enter the name of the task you want to delete: ")
                if task_to_delete in tasks:
                    tasks.remove(task_to_delete)
                    print(f"Task '{task_to_delete}' deleted successfully.")
                else:
                    print("Task not found. Please try again.")
            
            elif choice == 4:
                print("\nCurrent tasks:")
                for task in tasks:
                    print(f"- {task}")
            
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            
task_manager()
