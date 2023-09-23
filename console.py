#!/usr/bin/python3
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place 
from models.review import Review

class HBNBCommand(cmd.Cmd):
    classes = [
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review",
    ]

    prompt = '(hbnb) '

    def do_EOF(self, args):
        """EOF command to exit the program.
        """
        return True

    def do_quit(self, args):
        """Quit command to exit the program.
        """
        return True

    def emptyline(self):
        pass
    
    def do_create(self, args):
        list_args = args.split()
        if list_args:
            if list_args[0] in HBNBCommand.classes:
                new_instance = eval(list_args[0] + '()')
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")                  

    def do_show(self, args):
        list_args = args.split()
        if list_args:
            if list_args[0] not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            if len(list_args) > 1:
                key = list_args[0] + "." + list_args[1]
                if key in models.storage.all():
                    print(models.storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")        
        else:
            print("** class name missing **")

    def do_destroy(self, args):
        list_args = args.split()
        if list_args:
            if not list_args[0] in HBNBCommand.classes:
                print("** class doesn't exist **")
                return 
            if len(list_args) > 1: 
                key = list_args[0] + "." + list_args[1]
                if key in models.storage.all():
                    del models.storage.all()[key]
                    models.storage.save()
                else:
                    print("** no instance found **")                
            else:
                print("** instance id missing **")
        else:
            print("** clas name missing **")

    def do_all(self, args):
        list_args = args.split()
        if not list_args[0] in HBNBCommand.classes:
            print("** class doesn't exist **") 
            return         
        list_instances = []
        for key, value in models.storage.all().items():
            list_instances.append(str(value))
        print(list_instances)
    
    def do_update(self, args):
        list_args = args.split()
        if not list_args:
            print("** class name missing **")
            return
        if not list_args[0] in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(list_args) == 1: 
            print("** instance id missing **")
            return
        key = list_args[0] + "." + list_args[1]
        if not key in models.storage.all():
            print("** no instance found **")
        elif len(list_args) == 2:
            print("** attribute name missing **")             
        elif len(list_args) == 3:
            print("** value missing **")
        else:
            dictionary_key = list_args[2]
            dictionary_value = list_args[3]
            instance = models.storage.all()[key]
            setattr(instance, dictionary_key, dictionary_value)
            instance.save()
  
if __name__ == "__main__":
    HBNBCommand().cmdloop()