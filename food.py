class Food:
    def __init__(self, name):
        self.naming(name)

    def naming(self, name):
        self.name = name

    def show(self):
        print("This is", self.name)


class Fruit(Food):

    def show(self):
        print(f"This is {self.name}, it's a fruit")


class Citrus(Fruit):

    def show(self):
        print(f"This is {self.name}, it's a citrus fruit")

# m = Food("meat")
# m.show()
# a = Fruit("an apple")
# a.show()
# lem = Citrus("lemon")
# lem.show()


class WithNoChanges:
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return str(self.content)

    def __int__(self):
        if (isinstance(self.content, int) or isinstance(self.content, float)
                or isinstance(self.content, str) and self.content.isdigit()):
            return int(self.content)
        else:
            return 0

    def __float__(self):
        if (isinstance(self.content, int) or isinstance(self.content, float)
                or isinstance(self.content, str) and self.content.isdigit()):
            return float(self.content)
        else:
            return 0.0


# first = WithNoChanges("one")
# second = WithNoChanges("2")
# third = WithNoChanges(3)
# fourth = WithNoChanges(4.0)
# print("first:", str(first), int(first), float(first))
# print("second:", str(second), int(second), float(second))
# print("third:", str(third), int(third), float(third))
# print("fourth:", str(fourth), int(fourth), float(fourth))


class ListWithMerging:
    def __init__(self, lst: list):
        self.field = lst

    def __add__(self, obj):
        new_field = []
        for index in range(min(len(self.field), len(obj.field))):
            new_field += [self.field[index], obj.field[index]]

        if len(self.field) > len(obj.field):
            new_field += self.field[len(obj.field):]
        else:
            new_field += obj.field[len(self.field):]

        return ListWithMerging(new_field)

# a = ListWithMerging(["s"])
# b = ListWithMerging([4, 5, 6])
# c = a + b
# d = b + a
# e = a + c
# print("a:", a.field, "b:", b.field, "c = a + b", c.field, "d = b + a",
#      d.field, "e = a + c", e.field, sep="\n")


class StandardNumber:
    def __init__(self, number_: int):
        self.value = number_

    def __add__(self, n: int):
        self.value += n

    def __sub__(self, n: int):
        self.value -= n

    def __rsub__(self, n: int):
        self.value = n - self.value

    def __mul__(self, n: int):
        self.value *= n

    def __floordiv__(self, n: int):
        self.value //= n

# a = StandardNumber(80)
# print("a:", a.value)
# a + 5
# print("a + 5:", a.value)
# a - 5
# print("a - 5:", a.value)
# a // 5
# print("a // 5:", a.value)
# a * 5
# print("a * 5:", a.value)
# 5 - a
# print("5 - a:", a.value)


class Equality:
    def __init__(self, lst):
        self.data = lst

    def get_value(self, index):
        if len(self.data) < index:
            return 0
        else:
            return self.data[index - 1]        

    def __eq__(self, elem):
        return self.get_value(1) == elem.get_value(1)

    def __ne__(self, elem):
        return self.get_value(2) != elem.get_value(2)

    def __lt__(self, elem):
        return self.get_value(3) < elem.get_value(3)

    def __gt__(self, elem):
        return self.get_value(4) > elem.get_value(4)

    def __le__(self, elem):
        return self.get_value(5) <= elem.get_value(5)

    def __ge__(self, elem):
        return self.get_value(6) >= elem.get_value(6)

    
# a = Equality([1, 2, 3, 4, 5, 6])
# b = Equality([1, 1, 4, 3, 5, 6])
# c = Equality([])
# print(a == b, a != b, a < b, a > b, a <= b, a >= b, "\n", a == c, a != c, a < c, a > c, a <= c, a >= c)


class Initials:
    def __init__(self, field: list):
        self.field = [item for item in field if isinstance(item, str)]

    def __getattribute__(self, field):
        return [item[0] for item in object.__getattribute__(self, field)]

# me = Initials(["Natalia", "Tkachuk", 25, 12, 1992])
# print(me.field)
# print(object.__getattribute__(me, "field"))


def get_value(value, index):
    if len(value) <= index:
        return 0
    else:
        return value[index]


class Summary:
    def __init__(self, first=[], second=[]):
        self.first = first
        self.second = second

    def __getitem__(self, index):
        return get_value(self.first, index) + get_value(self.second, index)


# a = Summary([1, 2], [3, 4, 5])
# print(a.first)
# print(a.second)
# print(a[0], a[1], a[2], a[3])
# b = Summary([1, 2, 3])
# print(b.first)
# print(b.second)
# print(b[0], b[1], b[2], b[3])


class PolySum:
    def __init__(self, value=[]):
        self.value = value

    def polynomial(self, number_):
        result = 0
        for index, n in enumerate(self.value):
            result += number_ ** index * n

        return result

# a = PolySum([1, 2, 3])
# b = PolySum()
# print(a.value)
# print(a.polynomial(1), a.polynomial(2), b.polynomial(3))


class OddNumbers:
    def __init__(self, quantity: int):
        lst = []
        for i in range(quantity):
            lst.append(i * 2 + 1)

        self.lst = lst

    def __iter__(self):
        return iter(self.lst)


# a = OddNumbers(10)
# for number in a:
#    print(number)


class FibNumbers:
    def __init__(self, quantity: int):
        if quantity <= 2:
            self.lst = [1] * quantity
        else:
            lst = [1, 1]
            for i in range(2, quantity):
                lst.append(lst[i - 2] + lst[i - 1])

            self.lst = lst

    def __iter__(self):
        return iter(self.lst)


f = FibNumbers(20)
for number in f:
    print(number)
