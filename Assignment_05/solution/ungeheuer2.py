class Ungeheuer2:
    horrible = True

    def __init__(self, name, size, vulnerability, number_of_victims = 0):
        self.name = name
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

    def __str__(self):
        return f"{self.name} ({self.size}cm, {self.__number_of_victims} Opfer)"

if __name__ == "__main__":
    nightstalker = Ungeheuer2("Mage", 50, "heel")
    baby_monster = Ungeheuer2("Baby Monster", 20, "head")

    print(f"{nightstalker} verbreitet Angst und Schrecken")
    nightstalker.scare()

    print(f"{baby_monster} verbreitet Angst und Schrecken")
    baby_monster.scare()

    print(f"{nightstalker} bekommt Schlag an den Kopf")
    nightstalker.kampf("head")

    print(f"{baby_monster} bekommt Schlag an den Kopf")
    baby_monster.kampf("head")

    print(nightstalker)
    print(f"Size: {nightstalker.size}")
    print(f"Victims: {nightstalker.number_of_victims}")

    print(baby_monster)
    print(f"Size: {baby_monster.size}")
    print(f"Victims: {baby_monster.number_of_victims}")
