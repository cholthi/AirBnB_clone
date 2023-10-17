#!/usr/bin/python3
"""initialize models package directory"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
