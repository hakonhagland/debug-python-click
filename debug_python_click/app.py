import click

import sys
print("Early debug: Starting application", file=sys.stderr)

# Keep a reference to the original method
original_call = click.core.BaseCommand.__call__

# Define your new __call__ method
def new_call(self, *args, **kwargs):
    print("Custom __call__ invoked")
    #breakpoint()
    # Call the original behavior:
    return original_call(self, *args, **kwargs)

# Apply the monkey patch
click.core.BaseCommand.__call__ = new_call

@click.command()
@click.option('--name', default="World", help='Who to greet')
def greet(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    greet()
