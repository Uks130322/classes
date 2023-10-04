class Example:

    """Constructor"""
    def __init__(self, name, number=1):
        
        self.name = name
        if number == 1:
            self.next = None
        else:
            self.next = Example(self.name, number - 1)
        self.set()

    """Destructor"""
    def __del__(self):
        print("delete:", self.code)
            
    """Full the chain"""
    def set(self, num=1):
        self.code = self.name + "["+str(num)+"]"
        if self.next != None:
            self.next.set(num + 1)

    def show(self):
        print(self.code)
        if self.next != None:
            self.next.show()

    
print("one object")
a = Example("Alpha")
a.show()
print("chain of objects")
b = Example("Bravo", 5)
b.show()
print("from third")
b.next.next.show()
print("delete")
del a
del b



