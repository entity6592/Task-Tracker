import json
import sys
import os
from datetime import datetime
from zoneinfo import ZoneInfo

def load_tasks():
    if not os.path.exists("tasks.json"):
        return [] # Empty list = no tasks yet

    with open("tasks.json", "r") as file:
        tasks = json.load(file) # List of dictionaries
        return tasks
        
def save_tasks(tasks):  # Note: needs 'tasks' parameter
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)
        
def add_tasks(description, status="todo"):
    tasks = load_tasks()
    new_task = {
        "id": max(list(map(lambda x: x.get("id"), tasks)), default=0) + 1,
        "description": description,
        "createdAt": str(datetime.now(ZoneInfo("Europe/London"))),
        "updatedAt": str(datetime.now(ZoneInfo("Europe/London")))
    }
    if status == "done" or status == "in-progress":
        new_task["status"] = status
    elif status != "todo":
        raise ValueError("Invalid status: choose from todo, in-progress or done")
    else:
        new_task["status"] = "todo"
    
    tasks.append(new_task)
    save_tasks(tasks)
    return f"Task added successfully (ID: {new_task['id']})"

def list_tasks(status=""):
    tasks = load_tasks()

    if status == "done" or status == "todo" or status == "in-progress":
        filtered_tasks = list(filter(lambda x: x["status"]==status, tasks))
    elif status:
        raise ValueError("Invalid status: choose from todo, in-progress or done")
    else:
        filtered_tasks = tasks
    
    if not filtered_tasks:
        return f"No tasks saved - Type 'python3 main.py add [taskname]' to get started!"    

    tasklist = ""
    for item in filtered_tasks:
        tasklist += f"ID: {item['id']} | {item['description']} | Status: {item['status']} | Last modified: {item['updatedAt']}\n"
    return tasklist

def main():

    if len(sys.argv) < 2:
        print("Syntax: python3 main.py <command> [arguments]")
        return
    
    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Syntax: python3 main.py add 'task description'")
            return
        result = add_tasks(sys.argv[2])
        print(result)

    if command == "list":

        if len(sys.argv) > 2:
            result = list_tasks(status=sys.argv[2])
        else:
            result = list_tasks()
        print(result)


if __name__ == "__main__":
    main()