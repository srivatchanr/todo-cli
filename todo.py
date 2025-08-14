import json
import os
import sys

DATA_FILE = "todo.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)
    
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_tasks(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done":False})
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for i,task in enumerate(tasks):
        status = "[x]" if task["done"] else "[]"
        print(f"{i+1}.{status}{task['description']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    save_tasks(tasks)

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks.pop(index)
    save_tasks(tasks)

def edit_task(index, new_description):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["description"] = new_description
        save_tasks(tasks)

if __name__=="__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "add":
        add_tasks(" ".join(sys.argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done":
        mark_done(int(sys.argv[2]) - 1)
    elif cmd == "del":
        delete_task(int(sys.argv[2]) - 1)
    elif cmd == "edit":
        index = (int(sys.argv[2]) - 1)
        new_description = (" ".join(sys.argv[3:]))
        edit_task(index, new_description)
    else:
        print("Usage: python todo.py [add|list|done|del|edit] [args...]")