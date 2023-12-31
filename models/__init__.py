#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from os import getenv


"""Conditionally import either DBStorage or FileStorage"""
if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engin.file_storage import FileStorage
    storage = FileStorage()

"""Reload the storage after instantiation """
storage.reload()
