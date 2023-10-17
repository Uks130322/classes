from random import randrange


class User:
    """User's name and age"""
    
    def __init__(self, name="Noname", age="Noage"):
        """Creating element"""
        
        self.name = name
        self.age = age
        print("New user was created")

    def show(self):
        """Show element's atributes"""
        
        print("User name:", self.name, "\nUser age:", self.age)

    def __del__(self):
        """Delete element"""
        
        print("User", self.name, "was deleted")


class UnitedElements:
    """Summing of two int or str elements"""

    def __init__(self, first, second):
        """Creating element"""
        
        if isinstance(first, type(second)):
            self.result = first + second

    def show(self):
        """Show element's atributes"""
        print("Your list of numbers:", self.lst)

    def middle(self):
        """Find middle value"""
        return sum(self.lst) // len(self.lst)


def create(lst: list, name: str):
    """Create objects of class 'name'"""
    
    class SomeClass:
        """Class name"""

        def __init__(self):
            """Creating element"""
            
            for index, item in enumerate(lst):
                if isinstance(item, str):
                    self.__dict__[item] = index
                    
    SomeClass.__name__ = name
    
    return SomeClass()


def get_numbers(obj):
    """Create new object from obj with int values only"""
    
    new_obj = type(obj)()
    
    for key, value in obj.__dict__.items():
        if isinstance(value, int):
            new_obj.__dict__[key] = value

    return new_obj


class AnimalAge:
    """Age of animal"""

    def __init__(self, age: int):
        """Creating object of class"""
        
        self.age = age
        
    def show(self):
        """Show element's atributes"""
        
        return (self.__name__, self.age)


def create_animal(quantity):
    """Create list of tuples with animal name and age"""
    
    list_of_animals = []
    
    for i in range(quantity):
        name = input("Enter name of an animal: ")
        obj = AnimalAge(randrange(10) *2 + 1)
        obj.__name__ = name
        list_of_animals.append(obj.show())

    return list_of_animals


class ListOfNumbers:
    """Class with list of int numbers from some list"""
    
    def __init__(self, lst: list):
        """Create object"""
        
        self.lst = [item for item in lst if isinstance(item, int)]
        
        
def add_lists(list1, list2):
    """Create new object with list with elements equals sum
    of the lists"""
    
    new_list = type(list1)([])
    
    if len(list1.lst) < len(list2.lst):
        list1, list2 = list2, list1
        
    for index, item in enumerate(list1.lst):
        if index < len(list2.lst):
            new_list.lst.append(item + list2.lst[index])
        else:
            new_list.lst.append(item)

    return new_list
