class Flowers:
    def __init__(self, name, origin, description):
        self.name = name
        self.origin = origin
        self.description = description

    def show(self):
        print(f"The {self.name} is from {self.origin}, {self.description}")


class Rose(Flowers):
    def type(self):
        print("Floribunda, Patio, Ground cover, Climbing Rambling, Gallica")


class Lily(Flowers):
    def color(self):
        print("Peach, White, Red, Pink, Yellow")


class Tulip(Flowers):
    def size(self):
        print("Tulip plants can be between 10 and 70 cm")


class Orchid(Flowers):
    def smell(self):
        print("Smell of Orhid has been variously described as being like vanilla, baby powder, grape-like, or cocoa.")


rose = Rose("Rose", "Central Asia", "Roses are erect, climbing, or trailing shrubs")
lily = Lily("Lily", "Greek", " is the flower of Hera, wife of Zeus")
tulip = Tulip("Tulip", "Northern China and Southern Europe", " is the most popular of the spring-flowering bulbs")
orchid = Orchid("Orchid", "Greek", "like most flowers of monocots, has two whorls of sterile elements")

while True:
    choose_flower = input("Select the flower to see the description: Rose/Lily/Tulip/Orhid:or type 'off' to exit:")
    if choose_flower == 'off':
        break
    elif choose_flower == 'Rose':
        print(f"{rose.show()}\n {rose.type()}")
    elif choose_flower == 'Lily':
        print(f"{lily.show()}\n{lily.color()}")
    elif choose_flower == 'Tulip':
        print(f"{tulip.show()}\n {tulip.size()}")
    elif choose_flower == 'Orchid':
        print(f"{orchid.show()}\n {orchid.smell()}")
    else:
        print("You must to select the flower from the list:Rose/Lily/Tulip/Orhid.")