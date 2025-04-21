# Python TODO CLI Application

A simple command-line todo list application built with Python. The application uses JSON for task storage and provides basic task management functionality.

## Features

- Add new tasks with titles and optional descriptions
- List all tasks with their completion status
- Data persistence using JSON storage

## Installation

1. Clone this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Add a new task:
```bash
python src/todo.py add "Task title" -d "Optional task description"
```

List all tasks:
```bash
python src/todo.py list
```

Show help:
```bash
python src/todo.py --help
```