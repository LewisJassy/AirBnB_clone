#!/usr/bin/python3
# models/__init__.py
"""this is the doc string for models module
"""


from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()