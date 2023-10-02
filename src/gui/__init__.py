# gui/__init__.py

# Import the main window class for easier access from the package.
from .main_window import MainWindow

# If more GUI components are added to this package in the future,
# they can be imported here in a similar fashion for convenience.

# This approach simplifies the import path when the MainWindow class
# is needed outside the gui package. Instead of writing:
# `from gui.main_window import MainWindow`
# one can use:
# `from gui import MainWindow`