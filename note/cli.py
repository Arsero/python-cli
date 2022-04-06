from typing import Optional
import typer
from note import commands, __app_name__, __version__

app = typer.Typer()


@app.command()
def show():
    commands.show()


@app.command()
def add(note: str):
    commands.add(note)


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
