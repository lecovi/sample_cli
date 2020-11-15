from pier_mob import items
import typer
from .items import app as items
from .users import app as users


__version__ = "0.0.3.2"


app = typer.Typer()
app.add_typer(items, name="items")
app.add_typer(users, name="users")


@app.command()
def info():
    typer.secho("Pier Mob built with Typer and ♥️.", fg=typer.colors.WHITE, bold=True)


@app.command()
def version():
    typer.echo(f"Pier Mob v{__version__}")
