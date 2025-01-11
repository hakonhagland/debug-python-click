import click
import pdb

# Keep a reference to the original method if needed
original_call = click.core.BaseCommand.__call__

# Define your new __call__ method
def new_call(self, *args, **kwargs):
    # Insert your custom behavior here
    print("Custom __call__ invoked")
    # Optionally call the original behavior:
    return original_call(self, *args, **kwargs)

# Apply the monkey patch
click.core.BaseCommand.__call__ = new_call

@click.command()
@click.option('--name', default="World", help='Who to greet')
def greet(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    greet()
