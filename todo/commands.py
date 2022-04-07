from typing import List
import typer
import os
from todo.task import Task, TaskEncoder
import json
from rich.console import Console
from rich.table import Table
from todo import __filename__

filename = __filename__


def list():
    tasks = load_tasks(filename)
    table(tasks)


def add(content: str):
    tasks = load_tasks(filename)
    if len(tasks) == 0:
        id = 0
    else:
        id = tasks[-1].id + 1

    task = Task(id, content)
    tasks.append(task)
    save_tasks(filename, tasks)
    table([task])


def remove(id: int):
    tasks = load_tasks(filename)
    try:
        tasks.remove(Task(id))
        save_tasks(filename, tasks)
        typer.echo(typer.style("Task removed !", fg=typer.colors.YELLOW))
    except:
        typer.echo(typer.style("Task not found !", fg=typer.colors.YELLOW))


def remove_done():
    tasks = load_tasks(filename)
    try:
        tasks = [t for t in tasks if t.done == False]
        save_tasks(filename, tasks)
        typer.echo(typer.style("Tasks done removed !", fg=typer.colors.YELLOW))
    except:
        typer.echo(typer.style("No tasks !", fg=typer.colors.YELLOW))


def done(id: int):
    tasks = load_tasks(filename)
    try:
        index = tasks.index(Task(id))
        tasks[index].done = not tasks[index].done
        save_tasks(filename, tasks)
        table([tasks[index]])
    except:
        typer.echo(typer.style("Task not found !", fg=typer.colors.YELLOW))


def clear():
    save_tasks(filename, [])
    typer.echo(typer.style("All tasks removed!", fg=typer.colors.YELLOW))


def load_tasks(filename: str) -> List[Task]:
    try:
        with open(filename, "r") as f:
            text = f.read()
        if text:
            tasks = json.loads(text, object_hook=Task.from_json)
        else:
            tasks = []
    except:
        tasks = []

    return tasks


def save_tasks(filename: str, tasks: List[Task]):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write(json.dumps(tasks, indent=4, cls=TaskEncoder))


def table(tasks: List[Task]):
    console = Console()
    table = Table(show_header=True, header_style="bold cyan1")
    table.add_column("Id", justify="right")
    table.add_column()
    table.add_column("Task", justify="left")
    typer.echo("\n")
    for task in tasks:
        if task.done:
            table.add_row(str(task.id), "■", task.content)
        else:
            table.add_row(str(task.id), "─", task.content)

    console.print(table)
    typer.echo("\n")
