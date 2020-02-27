#!/usr/bin/python3
import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

my_class = {'BaseModel': BaseModel, 'User': User, 'State': State,
            'City': City, 'Amenity': Amenity, 'Place': Place,
            'Review': Review}


class HBNBCommand(cmd.Cmd):
    """ command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return(True)

    def emptyline(self):
        """Do not nothing"""
        pass

    def do_EOF(self, args):
        """Quit command to exit the program"""
        return(True)

    def do_create(self, args):
        """Creates a new instance of BaseModel"""
        if len(args) == 0:
            print("** class name missing **")
        else:
            if args in my_class:
                new_obj = my_class[args]()
                new_obj.save()
                print(new_obj.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, args):
        """Prints the string representation of an instance
        based on the class name and id"""

        my_dict = models.storage.all()
        split_args = get_args(args)

        if len(args) == 0:
            print("** class name missing **")
        else:
            if split_args[0] in my_class:
                if len(split_args) > 1:
                    my_search = split_args[0] + '.' + split_args[1]

                    if my_search in my_dict:
                        print(my_dict.get(my_search))

                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)"""

        my_dict = models.storage.all()
        split_args = get_args(args)

        if len(args) == 0:
            print("** class name missing **")
        else:
            if split_args[0] in my_class:
                if len(split_args) > 1:
                    my_search = split_args[0] + '.' + split_args[1]

                    if my_search in my_dict:
                        my_dict.pop(my_search)
                        models.storage.save()
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")

    def do_all(self, args):
        """Prints all string representation of all instances
        based or not on the class name"""

        my_dict = models.storage.all()
        split_args = get_args(args)
        my_list_obj = []

        if len(split_args) == 0 or split_args[0] in my_class:

            for key, value in my_dict.items():
                aux = str(value.__repr__)
                my_list_obj.append(aux[aux.find('['):len(aux)-1])

            print(my_list_obj)

        else:
            if split_args[0] not in my_class:
                print("** class doesn't exist **")

    def do_update(self, args):
        """Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file"""

        my_dict = models.storage.all()
        split_args = get_args(args)
        formt = "%Y-%m-%dT%H:%M:%S.%f"

        if len(args) == 0:
            print("** class name missing **")
        else:
            if split_args[0] in my_class:
                if len(split_args) > 1:
                    my_search = split_args[0] + '.' + split_args[1]

                    if my_search in my_dict:
                        if len(split_args) > 2:
                            if len(split_args) > 3:
                                my_search = split_args[0] + '.' + split_args[1]
                                if my_search in my_dict:
                                    value = my_dict.get(my_search)
                                    if split_args[2] == "created_at":
                                        setattr(value, split_args[2],
                                                datetime.strptime(
                                                    split_args[3], formt))
                                    elif split_args[2] == "updated_at":
                                        setattr(value, split_args[2],
                                                datetime.strptime(
                                                    split_args[3], formt))
                                    else:
                                        setattr(value, split_args[2],
                                                split_args[3])
                                    models.storage.save()
                                else:
                                    print("** no instance found **")
                            else:
                                print("** value missing **")
                        else:
                            print("** attribute name missing **")
                    else:
                        print("** no instance found **")
                else:
                    print("** instance id missing **")
            else:
                print("** class doesn't exist **")


def get_args(args):
    """split the args """
    return (args.split())

if __name__ == '__main__':
    HBNBCommand().cmdloop()
