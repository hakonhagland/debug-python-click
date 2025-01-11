import click

@click.command()
@click.option('--name', default="World", help='Who to greet')
def greet(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    greet()
