#!/usr/bin/env python
def main():
    Test1 = Temp(C=57)
    Test2 = Temp(C=98)
    Test3 = Temp(F=120)
    Test4 = Temp(F=35)
    print(Test1.F)
    print(Test2.K)
    print(Test3.C)
    print(Test4.K)


class Temp():
    def __init__(self, K=None, C=None, F=None):
        self.K = None
        try:
            if K != None and not (F or C):
                self.K = K
            elif F != None and not (K or C):
                K = (F - 32) * 5 / 9 + 273.15
                self.K = K
            elif C != None and not (F or K):
                K = C + 273.15
                self.K = K
            else:
                raise (RuntimeError('Kein Eingabewert!'))
            if self.K < 0:
                raise (RuntimeError('Nicht unter den absoluten 0 Punkt!'))
        except RuntimeError as e:
            self.K = None
            print(e, "Kein Wert eingetragen")

    @property
    def F(self):
        return ((self.K - 273.15) * 9 / 5) + 32

    @property
    def C(self):
        return (self.K - 273.15)


if __name__ == "__main__":
    main()
