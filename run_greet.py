# run_greet.py
import sys
print("Custom entry script started", file=sys.stderr)

from debug_python_click.app import greet  # Adjust this import to match your project's structure
sys.exit(greet())  # Execute the Click command directly

