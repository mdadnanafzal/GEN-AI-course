# class chai:
#     def __init__(self, flavor):
#         self.flavor = flavor
#     def brew(self):
#         print(f"Brewing chai: {self.flavor}")

# c1 = chai("Masala")
# c2 = chai("Ginger")
# print(c1.brew())
# print(c2.brew())

class Chaicup:
    size = 150
    
    def  describe(self):
        return f"A {self.size} ml chai cup"

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two))