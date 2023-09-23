#!/usr/bin/python3
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj): 
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj
    
    def save(self):
        dictionary = {}
        for key in self.__objects.keys():
            dictionary[key] = self.__objects.get(key).to_dict()
        with open(self.__file_path, mode='w', encoding="utf-8") as file:
            json.dump(dictionary, file) 

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, mode='r') as file:
                my_dict = json.loads(file.read())
            for k, v in my_dict.items():
                self.__objects[k] = eval(f"{v.get('__class__')}(**v)")
            