class Ungeheuer:
    horrible = True

    def __init__(self, size, vulnerability, number_of_victims = 0):
        self.size                = size # in cm
        self.__vulnerability     = vulnerability
        self.__number_of_victims = number_of_victims

    # number_of_victims nach außen lese- und schreibar machen
    @property
    def number_of_victims(self):
        return self.__number_of_victims

    @number_of_victims.setter
    def number_of_victims(self, value):
        self.__number_of_victims = value

    # Monster können wachsen
    def grow(self, growth):
        self.size = self.size + int(growth)

    def scare(self):
        if self.size >= 50:
            self.number_of_victims = self.number_of_victims + 1
            return True
        else:
            return False

    def kampf(self, target):
        if self.__vulnerability == target:
            self.grow(-10)
            return True
        else:
            return False

if __name__ == "__main__":
    nightstalker = Ungeheuer(50, "heel")
    baby_monster = Ungeheuer(20, "head")

    print("Night Stalker verbreitet Angst und Schrecken")
    nightstalker.scare()

    print("Baby Monster verbreitet Angst und Schrecken")
    baby_monster.scare()

    print("Night Stalker bekommt Schlag an den Kopf")
    nightstalker.kampf("head")

    print("Baby Monster bekommt Schlag an den Kopf")
    baby_monster.kampf("head")

    print("Night Stalker")
    print(f"Size: {nightstalker.size}")
    print(f"Victims: {nightstalker.number_of_victims}")

    print("Baby Monster")
    print(f"Size: {baby_monster.size}")
    print(f"Victims: {baby_monster.number_of_victims}")
