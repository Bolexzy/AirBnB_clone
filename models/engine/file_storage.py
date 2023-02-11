#!/usr/bin/python3
"""
    Defines a FileStorage class Module(JSON).
"""
import json


class FileStorage:
    """A class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    Attributes:
        __file_path (str): The path to the JSON file to save objects.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects, the object with key <obj_class_name>.id.
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file. """
        filename = FileStorage.__file_path
        with open(filename, "w") as json_file:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, json_file)

    def reload(self):
        """ Deserializes the JSON file to __objects """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.city import City
        from models.amenity import Amenity
        from models.state import State
        from models.review import Review

        filename = FileStorage.__file_path
        class_map = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                     'State': State, 'City': City, 'Amenity': Amenity,
                     'Review': Review}
        try:
            with open(filename, "r") as json_file:
                for obj in json.load(json_file).values():
                    self.new(class_map[obj['__class__']](**obj))
        except FileNotFoundError:
            pass
