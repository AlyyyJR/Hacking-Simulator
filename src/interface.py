from rich.console import Console
from rich.panel import Panel

console = Console()

def show_puzzle(puzzle):
    console.print(Panel.fit(f"[bold green]Défi : {puzzle['type']}[/]\n[italic]Indice : {puzzle['hint']}[/]", title="💻 Hacking Simulator"))

def show_result(success):
    if success:
        console.print("[bold green]✅ Réussi ![/]")
    else:
        console.print("[bold red]❌ Incorrect[/]")