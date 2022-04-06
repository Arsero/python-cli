from typing import Optional
import typer
from todo import commands, __app_name__, __version__

app = typer.Typer(help="Todo list CLI")


@app.command()
def list():
    """
    List all tasks.
    """
    commands.list()


@app.command()
def add(task: str):
    """
    Add a new task with TEXT.
    """
    commands.add(task)


@app.command()
def remove(index: Optional[int] = typer.Argument(-1)):
    """
    Remove a task with ID, remove all tasks done without ID.
    """
    if index > -1:
        commands.remove(index)
    else:
        commands.remove_done()


@app.command()
def done(index: int):
    """
    Check a task with ID.
    """
    commands.done(index)


@app.command()
def clear():
    """
    Clear all tasks.
    """
    commands.clear()


def _version_callback(value: bool) -> None:

    if value:

        typer.echo(f"{__app_name__} v{__version__}")

        raise typer.Exit()


@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:

    return
