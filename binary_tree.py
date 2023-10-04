class BinaryTree:
    """Binary tree"""

    def __init__(self, number=1):
        """Create tree"""

        self.floor = number
        self.name = None

        if number == 1:            
            self.left = None
            self.right = None            
            
        else:
            self.left = BinaryTree(number - 1)
            self.right = BinaryTree(number - 1)
        self.index()


    def __del__(self):
        """Delete tree"""
        print(self.name, " was deleted")

        
    def index(self):
        """Numerate branches"""
        
        if self.left is not None:
            
            if self.name is None:
                self.name = str(1)         
            self.left.name = str(int(self.name) * 2)
            self.right.name = str(int(self.name) * 2 + 1)            
            self.left.index()            
            self.right.index()

            
    def full_dict(self, dict_for_print = dict()):
        """Create a dict to show the tree"""

        first_time = True

        dict_for_print.setdefault(self.floor, []).append(self.name)
        if self.left is not None:
            self.left.full_dict(dict_for_print)
            self.right.full_dict(dict_for_print)

        return dict_for_print

       
    def show(self):
        """Show tree"""
        
        for key, value in self.full_dict(dict()).items():
            print(f"floor {key}: {value}")


def create_chain(quantity):
    return BinaryTree(quantity)

tree = create_chain(3)
tree.show()
print("\n")

tree2 = create_chain(4)
tree2.show()

print("left")
tree.left.show()

print("right left")
tree.right.left.show()
