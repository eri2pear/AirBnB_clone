"""__init__ method for models directory"""
from models.engine.file_storage.py import FileStorage


storage = FileStorage()
storage.reload()
