import json
import sys
import os
from datetime import datetime
from zoneinfo import ZoneInfo

# Read tasks from json into variable
def load_tasks():
    if not os.path.exists("tasks.json"):
        return [] # Creates the json for compatibilty if it doesn't yet exist

    with open("tasks.json", "r") as file:
        tasks = json.load(file)
        return tasks
        
# Write new task list to json
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)


def add_task(description, status="todo"):

    # Initalise the task list variable inside the function
    tasks = load_tasks()
    new_task = {
        "id": max(list(map(lambda x: x.get("id"), tasks)), default=0) + 1,
        "description": description,
        "createdAt": str(datetime.now(ZoneInfo("Europe/London"))),
        "updatedAt": str(datetime.now(ZoneInfo("Europe/London")))
    }

    # Allows for initialisation with a different status but checks for invalid statuses
    if status == "done" or status == "in-progress":
        new_task["status"] = status
    elif status != "todo":
        raise ValueError("Invalid status: choose from todo, in-progress or done")
    else:
        new_task["status"] = "todo"
    
    tasks.append(new_task)

    # Write updated task list back to json
    save_tasks(tasks)
    return f"Task added successfully (ID: {new_task['id']})"

def delete_task(id):
    tasks = load_tasks()

    # Finds the task with matching ID
    for item in tasks:
        if item["id"] == id:
            tasks.remove(item)
            save_tasks(tasks)
            return f"Task ID {id} successfully deleted"
        
    # For-loop exits function if ID exists in tasks - catch any exceptions here
    return f"Task with ID {id} not found"

def update_task(id, new_description):
    tasks = load_tasks()

    # Finds the task with matching ID
    for item in tasks:
        if item["id"] == id:
            item["description"] = new_description
            item["updatedAt"] = str(datetime.now(ZoneInfo("Europe/London")))
            save_tasks(tasks)
            return f"Task ID {id} updated --> {new_description}"
    
    # For-loop exits function if ID exists in tasks - catch any exceptions here
    return f"Task with ID {id} not found"

def change_status(id, new_status):
    tasks = load_tasks()

    # Finds the task with matching ID
    for item in tasks:
        if item["id"] == id:
            item["status"] = new_status
            item["updatedAt"] = str(datetime.now(ZoneInfo("Europe/London")))
            save_tasks(tasks)
            return f"Task ID {id} now set to {new_status}"
        
    # For-loop exits function if ID exists in tasks - catch any exceptions here
    return f"Task with ID {id} not found"


def list_tasks(status=""):
    tasks = load_tasks()

    # If status variable is specified and valid, filters tasks by that status
    if status in ['done', 'todo', 'in-progress']:
        filtered_tasks = list(filter(lambda x: x["status"]==status, tasks))
    elif status:
        raise ValueError("Invalid status: choose from todo, in-progress or done")
    else:
        filtered_tasks = tasks
    
    # Accounts for no extant tasks (or tasks of the specified status)
    if not filtered_tasks:
        return f"No tasks saved - Type 'python3 main.py add [taskname]' to get started!"    

    # Formats the task list for print output
    tasklist = ""
    for item in filtered_tasks:
        tasklist += f"ID: {item['id']} | {item['description']} | Status: {item['status']} | Last modified: {item['updatedAt']}\n"
    tasklist = tasklist[:-1]
    return tasklist

def main():

    # Since all valid commands have at least python3 main.py <command>, catch this
    if len(sys.argv) < 2:
        print("Syntax: python3 main.py <command> [arguments]")
        return
    
    # Parse key command variable
    command = sys.argv[1]

    if command == "add":
        # Accounts for unexpected extra arguments
        if len(sys.argv) < 3:
            print("Syntax: python3 main.py add [task description]")
            return
        result = add_task(sys.argv[2])
        print(result)

    if command == "list":
        # Accounts for the inclusion of an optional status argument
        if len(sys.argv) > 2:
            result = list_tasks(status=sys.argv[2])
        else:
            result = list_tasks()
        print(result)

    if command == "delete":
        # Dirtily filters for incorrect command lengths
        if len(sys.argv) != 3:
            print("Syntax: python3 main.py delete [task ID]")
            return
        
        # Catches id inputs which are not integers
        try:
            id = int(sys.argv[2])
        except ValueError:
            print("Error: task ID must be an integer")
            return
        result = delete_task(id)
        print(result)

    if command == "update":       
        # Dirtily filters for incorrect command lengths
        if len(sys.argv) != 4:
            print("Syntax: python3 main.py update [task ID] <new task description>")
            return
        
        # Catches id inputs which are not integers
        try:
            id = int(sys.argv[2])
        except ValueError:
            print("Error: task ID must be an integer")
            return
        result = update_task(id, sys.argv[3])
        print(result)

    if command == "mark":
        # Dirtily filters for incorrect command lengths
        if len(sys.argv) != 4:
            print("Syntax: python3 main.py mark [task ID] <status>")
            return
        
        # Catches id inputs which are not integers
        try:
            id = int(sys.argv[2])
        except ValueError:
            print("Error: task ID must be an integer")
            return
        
        if sys.argv[3] not in ["todo", "in-progress", "done"]:
            print("Invalid status: choose from todo, in-progress or done")
            return
        result = change_status(id, sys.argv[3])
        print(result)

# Only runs main() if main.py is executing this script (i.e. not imported somewhere else)
if __name__ == "__main__":
    main()