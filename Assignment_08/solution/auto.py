class Auto:
    def __init__(self, name, kw, vmax):
        self.v = 0
        self.kw = kw
        self.vmax = vmax
        self.name = name

    def beschleunigen(self):
        vneu = self.v + self.kw * 0.1
        if (vneu > self.vmax):
            vneu = self.vmax
        self.v = vneu

class Hybrid(Auto):

    def __init__(self, name, kw, vmax):
        super().__init__(name, kw, vmax)
        self.cap = 10000 # Wh

class EAuto(Auto):
    pass

golf    = Auto("Golf GTI V6", 100, 180)
porsche = Hybrid("911 Turbo", 200, 250)

print(f"{golf.name} fährt {golf.v} km/h")
golf.beschleunigen()
print(f"{golf.name} fährt {golf.v} km/h")

print(f"{porsche.name} fährt {porsche.v} km/h")
porsche.beschleunigen()
print(f"{porsche.name} fährt {porsche.v} km/h, {porsche.cap}")
