from typing import List
import typer
from definition import __app_name__, __version__
from larousse_api import larousse
from rich.console import Console

console = Console()
app = typer.Typer(help="Definition CLI")


@app.command()
def main(word: str):
    """
    Get a definition for a WORD
    """
    if not word:
        typer.echo(f"{__app_name__} v{__version__}")
    else:
        response = larousse.get_definitions(word)
        typer.echo("\n")
        if len(response) > 0:
            display(response)
        else:
            typer.echo(f"\tNo definition found.")

        typer.echo("\n")

    return


def display(definitions: List[str]):
    for definition in definitions:
        typer.echo(definition)
