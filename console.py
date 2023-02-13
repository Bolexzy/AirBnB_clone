#!/usr/bin/python3
"""
    Defines a HBNBCommand class using the cmd module.
"""
import cmd
import re
import ast
import json
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
        methods defined:
            <class name>.show(<id>).
            <class name>.destroy(<id>).
            <class name>.update(<id>, <attribute name>, <attribute value>).

        """
        map_method = ['all', 'show', 'destroy', 'count', 'update']
        match = re.search(r'^(\w+)\.(\w+)(?:\(([^)]*)\))$', line)
        if match:
            class_name = match.group(1)
            cmd_method = match.group(2)
            cmd_args = match.group(3)
            if cmd_args is None:
                print("** instance id missing **")
                return ""
            match_attr = re.search('^"([^"]*)"(?:, (.*))?$', cmd_args)
            uid = cmd_args.strip('"')
            attr_and_value = ""

            if (class_name in HBNBCommand.class_map):
                if (cmd_method in map_method):
                    command = cmd_method + " " + class_name + " "
                    if cmd_method == 'update':
                        if match_attr and len(match_attr.groups()) > 0:
                            uid = match_attr.group(1)
                            attr = match_attr.group(2)
                            if attr is None:
                                attr = ""
                            match_dict = re.search('^({.*})$', attr)
                            match_attr_value = re.search(
                                '^(?:"([^"]*)")?(?:, (.*))?$', attr)

                            if match_dict:
                                self.do_update_dict(class_name,
                                                    uid, match_dict.group(1))
                                command = ""
                                return ""
                            elif match_attr_value \
                                    and len(match_attr_value.groups()) > 1:
                                attr_name = (match_attr_value.group(1) or "")
                                attr_value = (match_attr_value.group(2) or "")
                                attr_and_value = attr_name + " " + attr_value
                        command += uid + " " + attr_and_value
                    else:
                        command += uid
                    self.onecmd(command)
        return False

    def do_create(self, name):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        if not name:
            print("** class name missing **")
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
        """Usage: show <class_name> <id> - prints instance info(str).
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

        reg = r'(\w+)(?:\s(\S+)(?:\s(\w+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(reg, line)

        if match:
            class_name = match.group(1)
            uid = match.group(2)
            attr = match.group(3)
            value = match.group(4)

        if not line or not match:
            print("** class name missing **")
        elif class_name not in HBNBCommand.class_map:
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(class_name, uid.strip('"'))
            if key not in obj_dict:
                print("** no instance found **")
            else:
                if not attr:
                    print("** attribute name missing **")
                elif not value:
                    print("** value missing **")
                else:
                    casttype = str
                    try:
                        casttype = type(ast.literal_eval(value))
                    except (ValueError, SyntaxError):
                        pass
                    value = value.replace('"', '')
                    setattr(storage.all()[key], attr, casttype(value))
                    storage.all()[key].save()

    def do_update_dict(self, class_name, uid, dict_attr):
        """Update method for attr, value pairs in a dict.
        """
        if uid is None:
            print("** instance id missing **")

        strip_dict = dict_attr.replace("'", '"')
        d = json.loads(strip_dict)

        key = "{}.{}".format(class_name, uid)

        if key not in storage.all():
            print("** no instance found **")

        for k, v in d.items():
            update_args = f'{class_name} {uid} {k} {v}'
            result = self.do_update(update_args)
            if result is not None:
                break

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, line):
        return True

    def help_quit(self):
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        print()
        return True

    help_EOF = help_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
