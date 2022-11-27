#!/usr/bin/python3

"""This initialises Global Variables"""

from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
