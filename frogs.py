class Frogs:
    """Frogs"""

    def __init__(self, number=0):
        """Create frog"""
        if number == 0:
            self.next = None
            self.index()
        else:
            self.next = Frogs(number - 1)

        


    def __del__(self):
        """Delete frog"""
        print(self.name, " was deleted")


    def index(self):
        """Numerate frogs"""
        
        i = 0
        while self.next is not None:
            self.name = f"Frog_{i}"
            self = self.next
            i += 1
        else:
            self.name = f"Frog_{i}"

        
    def show(self):
        """Show frog"""

        while self.next is not None:
            self = self.next
            print(self.name)
            

    def insert_frog(self, where):
        """Insert frog in the chain"""
        
        print(f"New frog was added after Frog {where}")

        for i in range(where):
            self = self.next
    
        place = self.next
        self.next = Frogs()
        self.next.name = "New_frog"
        self.next.next = place


    def delete_frog(self, which):
        """Delete frog from the chain"""
        print(f"Frog {which} was deleted")

        for i in range(which - 1):
            self = self.next
        
        if self.next is not None:
            self.next = self.next.next
        else:
            self.next = None
        return self


def create_chain(quantity):
    return Frogs(quantity)

u = create_chain(6)
u.show()
u.insert_frog(6)
u.show()
u.insert_frog(0)
u.show()
u.insert_frog(3)
u.show()
u.delete_frog(1)
u.show()
u.delete_frog(3)
u.show()
u.delete_frog(7)
u.show()
