# To-Do List App
tasks = []
def add_task(task): tasks.append(task); print(f"Added: {task}")
def list_tasks(): print("\n".join(f"{i+1}. {t}" for i, t in enumerate(tasks)) or "No tasks")
while True:
    cmd = input("Enter command (add/list/exit): ")
    if cmd == "add": add_task(input("Task: "))
    elif cmd == "list": list_tasks()
    elif cmd == "exit": break
