# Task-Tracker

## Description

A Python3 script used to manage your tasks via the Command Line Interface (CLI).

User inputs are taken as arguments, and tasks are stored in a JSON file - this will be created automatically when one doesn't exist.

Each task has:

- A unique ID number
- A description
- Time of creation
- Time most recently modified (defaulted to time of creation)
- Completion status (todo, in-progress, or done)

## Getting Started

Requires Python 3.x installed. Navigate to the appropriate directory. Type commands into the terminal. For example:

**Add your first task:**
```bash
python3 main.py add "buy groceries"
```
```
Task added successfully (ID: 1)
```

**Update a task description:**
```bash
python3 main.py update 1 "buy groceries and make dinner"
```
```
Task ID 1 updated --> buy groceries and make dinner
```

**Mark a task as completed:**
```bash
python3 main.py mark 1 done
```
```
Task ID 1 now set to done
```

**List all completed tasks:**
```bash
python3 main.py list done
```
```
ID: 1 | buy groceries and make dinner | Status: done | Last modified: 2025-06-24 18:23:51.016109+01:00
```

## Command List

**Add task:**
```bash
python3 main.py add <task description>
```

**Update task description:**
```bash
python3 main.py update <ID> <new description>
```

**Delete task:**
```bash
python3 main.py delete <ID>
```

**Mark task as todo, in-progress or done:**
```bash
python3 main.py mark <ID> <new status>
```

**List tasks (optional: filter by status):**
```bash
python3 main.py list <OPTIONAL status filter>
```

**This project is from roadmap.sh**

https://roadmap.sh/projects/task-tracker