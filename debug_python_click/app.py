import click
import pdb

class DebugCommand(click.Command):
    def format_help(self, ctx, formatter):
        pdb.set_trace()  # Breakpoint here
        return super().format_help(ctx, formatter)

@click.command(cls=DebugCommand)
@click.option('--name', default="World", help='Who to greet')
def greet(name):
    click.echo(f"Hello, {name}!")

if __name__ == "__main__":
    greet()
