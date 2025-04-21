import pytest
import os
import json
from todo import add_task, list_tasks, mark_complete, TASKS_FILE
from unittest.mock import patch
from io import StringIO

@pytest.fixture
def temp_tasks_file(tmp_path):
    original_tasks_file = TASKS_FILE
    temp_file = tmp_path / "test_tasks.json"
    with patch('todo.TASKS_FILE', str(temp_file)):
        yield str(temp_file)
    if os.path.exists(temp_file):
        os.remove(temp_file)

def test_add_task(temp_tasks_file):
    # Test adding a task
    add_task("Test task", "Test description")
    
    # Verify the task was added correctly
    with open(temp_tasks_file, 'r') as f:
        tasks = json.load(f)
    
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test task"
    assert tasks[0]["description"] == "Test description"
    assert not tasks[0]["completed"]
    assert tasks[0]["id"] == 1

def test_list_tasks(temp_tasks_file, capsys):
    # Add some test tasks
    add_task("Task 1", "Description 1")
    add_task("Task 2", "Description 2")
    
    # Test listing tasks
    list_tasks()
    captured = capsys.readouterr()
    
    # Verify output contains task information
    assert "[ ] 1. Task 1" in captured.out
    assert "Description 1" in captured.out
    assert "[ ] 2. Task 2" in captured.out
    assert "Description 2" in captured.out

def test_mark_complete(temp_tasks_file):
    # Add a test task
    add_task("Test task")
    
    # Mark it as complete
    mark_complete("1")
    
    # Verify the task was marked as complete
    with open(temp_tasks_file, 'r') as f:
        tasks = json.load(f)
    
    assert tasks[0]["completed"]

def test_mark_complete_invalid_id(temp_tasks_file, capsys):
    # Test marking non-existent task
    mark_complete("999")
    captured = capsys.readouterr()
    assert "Error: Task 999 not found" in captured.out
    
    # Test marking with invalid input
    mark_complete("abc")
    captured = capsys.readouterr()
    assert "Error: Task ID must be a valid number" in captured.out