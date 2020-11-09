class Mouse:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("squeak")


class Cat:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Meow")


class Horse:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Neigh")


class Goat:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("bleat")


class Cow:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("moo")


class Donkey:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("hee-haw")


class Lion:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Roar")


class Bear:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Growl")


class Elephant:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Trumpet")


class Frogs:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Croak")


class Giraffe:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Bleat")


class Dolphin:
    noOfEyes = 2

    def __init__(self, noOfFins, name):
        # public specifier
        self.noOfFins = noOfFins
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Click")


class Duck:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("quack")


class Penguin:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("noot noots")


class Dog:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Barks")


class Kangaroos:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("chortle")


class Monkey:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Chatter")


class Rabbit:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("drums")


class Pig:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Snorts")


class Fox:
    noOfEyes = 2

    def __init__(self, noOfLegs, name):
        # public specifier
        self.noOfLegs = noOfLegs
        # private specifier
        self.__name = name

    def printName(self):
        print(self.__name, end=" ")

    def speak(self):
        print("Yelps")


mouse1 = Mouse(4, "jerry")
mouse1.printName()
print("says", end=" ")
mouse1.speak()
print("It has", mouse1.noOfLegs, "legs and", mouse1.noOfEyes, "eyes")

# destructor
del mouse1
