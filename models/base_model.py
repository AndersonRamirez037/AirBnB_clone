#!/usr/bin/python3

import uuid
from datetime import datetime
import models

time_format = "%Y-%m-%dT%H:%M:%S.%f"
class BaseModel():
    def __init__(self,*args, **kwargs):

        if kwargs:
            for key, value in kwargs.items():    
                if key == "__class__":
                    continue
                elif key == "created_at":
                    self.created_at = datetime.strptime(kwargs["created_at"], time_format)
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(kwargs["updated_at"],time_format)
                else: 
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()
        return dictionary 