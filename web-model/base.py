#!/usr/bin/python3
"""
This module contains all the common features of the
other class that will import it
"""
import uuid
from datetime import datetime


class Base:
    """Base class with all the common attributes/methods
    this class should have 3 instance attributes
        - id (str)
        - created_at (str)
        - updated_at (str)
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        # Overwrite the attribute values to new values
        if kwargs:
            for attr, val in kwargs.items():
                if attr in ['created_at', 'updated_at']: # change the default values
                    setattr(self, attr, val)
                elif attr != '__class__': # ignore the class attribute
                    setattr(self, attr, val)
        
        # special method called __str__ in python
