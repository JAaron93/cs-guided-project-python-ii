class Animal:
    name = ""
    kind = ""
    color = ""

    def description(self):
        return "%s is a %s %s." % (self.name, self.color, self.kind)

# Create instances of Animal here and modify the instance attributes as described above.


cat = Animal()
cat.name = "Purrrfect"
cat.kind = "cat"
cat.color = "brown"

dog = Animal()
dog.name = "Fido"
dog.kind = "dog"
dog.color = "black"

print(cat.description())
