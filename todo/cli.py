from typing import Optional
import typer
from todo import commands, __app_name__, __version__

app = typer.Typer()


@app.command()
def list():
    commands.list()


@app.command()
def add(task: str):
    commands.add(task)


@app.command()
def remove(index: Optional[int] = typer.Argument(-1)):
    if index > -1:
        commands.remove(index)
    else:
        commands.remove_done()


@app.command()
def done(index: int):
    commands.done(index)


@app.command()
def clear():
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
