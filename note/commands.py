import typer
import os
from note import __filename__
from datetime import date

filename = __filename__


def show():
    try:
        notes = read_notes(filename)
        if not notes:
            typer.echo(f"No notes !")
        else:
            typer.echo("\n" + notes)
    except:
        typer.echo(f"No notes !")


def add(note: str):
    today = date.today()
    complete_note = "[" + str(today) + "] " + note + "\n"

    add_note(filename, complete_note)
    typer.echo("\nNote added : " + complete_note)


def clear():
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        f.write("")

    typer.echo(typer.style("All notes removed!", fg=typer.colors.YELLOW))


def read_notes(filename: str) -> str:
    try:
        with open(filename, "r") as f:
            text = f.read()
    except:
        text = ""

    return text


def add_note(filename: str, note: str):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "a") as f:
        f.write(note)
