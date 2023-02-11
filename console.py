#!/usr/bin/python3
"""
    Defines a HBNBCommand class using the cmd module.
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """Basic command line interpreter 'hbnb$'.
    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "
    class_map = ['BaseModel', 'User', 'Amenity',
                 'Place', 'City', 'State', 'Review']

    def default(self, line):
        """Executes a user input that does not match other defined methods.
        """
        map_method = ['all', 'show', 'destroy', 'count', 'update']
        match = re.search(r'^(\w+)\.(\w+)(?:\(([^)]*)\))$', line)
        if match:
            class_name = match.group(1)
            cmd_method = match.group(2)
            cmd_args = match.group(3).strip('"')
            print(cmd_args)

            if (class_name in HBNBCommand.class_map):
                if (cmd_method in map_method):
                    command = cmd_method + " " + class_name + " " + cmd_args
                    self.onecmd(command)
        return False

    def do_create(self, name):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        if not name:
            print("*** class name missing **")
        elif name not in HBNBCommand.class_map:
            print("** class doesn't exist **")
        else:
            map_dict = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                        'City': City, 'Amenity': Amenity, 'State': State,
                        'Review': Review}
            obj = map_dict[name]()
            storage.new(obj)
            print("{}".format(obj.id))
            obj.save()

    def do_show(self, line):
        """Usage: show <class_name> <id>
        Prints the string representation of a class instance of a given id.
        """
        obj_dict = storage.all()
        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in HBNBCommand.class_map:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in obj_dict:
                    print("** no instance found **")
                else:
                    print(obj_dict[key])

    def do_destroy(self, line):
        """Usage: destroy <class_name> <id>
        Deletes an instance based on the class name and id
        """
        obj_dict = storage.all()

        if not line:
            print("** class name missing **")
        else:
            args = line.split()
            if args[0] not in HBNBCommand.class_map:
                print("** class doesn't exist **")
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in obj_dict:
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Usage: $ all <class_name> or $ all
        Prints all string representation of all instances
        based or not on the class name
        """
        args = line.split()
        obj_dict = storage.all()
        if len(args) > 0:
            if args[0] not in HBNBCommand.class_map:
                print("** class doesn't exist **")
            else:
                obj_list = []
                for obj in obj_dict.values():
                    if args[0] == type(obj).__name__:
                        obj_list += [obj.__str__()]
                print(obj_list)
        elif len(args) == 0:
            obj_list = [str(obj) for key, obj in obj_dict.items()]
            print(obj_list)

    def do_count(self, line):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a class.
        """
        count = 0
        args = line.split()

        for obj in storage.all().values():
            if type(obj).__name__ == args[0]:
                count += 1
        print(count)

    def do_update(self, line):
        """Usage: update <class_name> <id> <attribute name> "<attribute value>"
        Updates an instance attribute based on the class name and id
        """
        obj_dict = storage.all()

        match = re.findall(r'(\w+) (\w+-\w+-\w+-\w+-\w+) (\w+) "(.*?)"', line)
        args = list(match[0])

        if not line:
            print("** class name missing **")
        elif len(args) > 0:
            if args[0] not in HBNBCommand.class_map:
                print("** class doesn't exist **")
                print(args)
            elif len(args) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1].strip('"'))
                if key not in obj_dict:
                    print("** no instance found **")
                    print(args)
                else:
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        attr = args[2]
                        valtype = type(args[3])
                        setattr(storage.all()[key], attr, valtype(args[3]))
                        storage.all()[key].save()

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    do_EOF = do_quit
    help_EOF = help_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
