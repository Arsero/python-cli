import typer
from translate import __app_name__, __version__
from rich.console import Console
from googletrans import Translator

console = Console()
app = typer.Typer()


@app.command()
def main(word: str):
    if not word:
        typer.echo(f"{__app_name__} v{__version__}")
    else:
        typer.echo("\n")

        translator = Translator()
        trans_text = translator.translate(word, src='en', dest='fr')
        if not trans_text.text:
            typer.echo(f"Error when translating")
        else:
            typer.echo(trans_text.text)

        typer.echo("\n")

    return
