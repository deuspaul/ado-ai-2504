#!/usr/bin/env python3

import argparse
import json
import os
from datetime import datetime
from typing import List, Dict

TASKS_FILE = "tasks.json"

def load_tasks() -> List[Dict]:
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks: List[Dict]):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(title: str, description: str = "") -> None:
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "description": description,
        "created_at": datetime.now().isoformat(),
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added: {title}")

def list_tasks() -> None:
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        status = "✓" if task["completed"] else " "
        print(f"[{status}] {task['id']}. {task['title']}")
        if task["description"]:
            print(f"   {task['description']}")

def main():
    parser = argparse.ArgumentParser(description="Simple TODO list CLI application")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # Add task command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("-d", "--description", help="Task description", default="")

    # List tasks command
    subparsers.add_parser("list", help="List all tasks")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.title, args.description)
    elif args.command == "list":
        list_tasks()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()