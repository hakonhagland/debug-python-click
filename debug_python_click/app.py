import click
import pdb

# Save the original get_help method
original_get_help = click.core.Command.get_help

# Define a patched version
def patched_get_help(self, ctx):
    print("DEBUG: Entering get_help()")
    result = original_get_help(self, ctx)
    print("DEBUG: Exiting get_help()")
    return result

# Apply the monkey patch
click.core.Command.get_help = patched_get_help

@click.command()
@click.option('--name', default="World", help='Who to greet')
def greet(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    greet()
