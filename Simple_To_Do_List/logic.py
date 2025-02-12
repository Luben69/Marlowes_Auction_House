tasks = []


def add_task(task_to_add):
    if not task_to_add.strip():
        return f'The task should not be empty'
    if task_to_add not in tasks:
        tasks.append(task_to_add)
        return f'The task "{task_to_add}" was added to the to-do-list'
    else:
        return f'The task: "{task_to_add}" is already in the to-do-list!'


def delete_task(task_to_delete):
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
        return f'The task "{task_to_delete}" was deleted from the to-do-list'
    else:
        return f'The task: "{task_to_delete}" is not in the to-do-list!'


def give_current_info():
    if tasks:
        for n, t in enumerate(tasks, 1):
            print(f"{n}: {t}")
    else:
        return 'Your to-do-list is empty!'


while True:
    print("What do you want to do?:\n"
          "[1] to add task\n"
          "[2] to delete task\n"
          "[3] give info about the to-do-list\n"
          "[4] exit"
          "-----------------------------")

    try:
        command = int(input())
        if command == 1:
            print("What task to be added?:\n")
            task = input()
            print(add_task(task))
        elif command == 2:
            print("Which task to be deleted?:\n")
            task = input()
            print(delete_task(task))
        elif command == 3:
            print(give_current_info())
        elif command == 4:
            print("Alright")
            exit()
        else:
            print("not all commands are available for now")
    except ValueError:
        print("invalid input")
