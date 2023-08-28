# AirBnB Clone

The Aribnb clone will be a copy of the [Airbnb](https://www.airbnb.com/).

We will create a console to manage objects of our project.


## Features

### Command Interpreter

#### Description

The Command Interpreter is used to manage the whole application's functionality from the command line, such as:
+ Crete a new object.
+ Update object's attributes.
+ Destroy an object.

#### Usage

Commands | Description | Usage
-------- | ----------- |-------- |
**help** or **?**| Displays the documented commands. | **help**
**quit**     | Exits the program. | **quit**
**EOF**      | Ends the program. Used when files are passed into the program. | **EOF**
**create**  | Creates a new instance of the \<class_name\>. Creates a Json file with the object representation. and prints the id of created object. | **create** \<class_name\>
**show**    | Prints the string representation of an instance based on the class name and id. | **show** \<class_name class_id\>
**destroy** | Deletes and instance base on the class name and id. | **destroy** \<class_name class_id\>
**all** | Prints all string representation of all instances based or not on the class name | **all** or **all** \<class_name class_id\>
**update** | Updates an instance based on the class name and id by adding or updating attribute | **update** \<class_name class_id key value\>

## Execution
The shell should work like this in interactive mode:
#### Interactive Mode 
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: 
#### Non-Interactive Mode 
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Test

## Author
* **Anderson Ramírez** <[AndersonRamirez037](https://github.com/AndersonRamirez037)>
* **Juan Hoyos** <[jum200922004](https://github.com/jum20092004)>