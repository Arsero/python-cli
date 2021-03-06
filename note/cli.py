from typing import Optional
import typer
from note import commands, __app_name__, __version__

app = typer.Typer(help="Note fast CLI")


@app.command()
def show():
    """
    Show all notes.
    """
    commands.show()


@app.command()
def add(note: str):
    """
    Add a new note with TEXT.
    """
    commands.add(note)


@app.command()
def clear():
    """
    Clear all notes.
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
