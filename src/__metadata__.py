"""Metadata for the Project."""
from __future__ import annotations

import importlib.metadata

__all__ = ["__version__", "__project__"]

__version__ = importlib.metadata.version("python-reddit")
"""Version of the project."""
__project__ = importlib.metadata.metadata("python-reddit")["Name"]
"""Name of the project."""
