def teilen(*inputs):
    if len(inputs) == 1:
        return teilen_intern(inputs[0])
    elif len(inputs) == 2:
        s1 = inputs[0]
        s2 = inputs[1]
        s1l, s1r = teilen_intern(s1)
        s2l, s2r = teilen_intern(s2)
        return (s1l + s2l, s1r + s2r)
    else:
        return ("", "")

def teilen_intern(input):
    laenge = len(input)
    mitte = laenge // 2

    if laenge % 2:
        mitte = mitte + 1

    links = input[0:mitte]
    rechts = input[mitte:]

    return (links, rechts)

s = "abcde"
vorne, hinten = teilen(s)
print(f"Input: {s}, Vorne: {vorne}, hinten {hinten}")

s = "abcd"
vorne, hinten = teilen(s)
print(f"Input: {s}, Vorne: {vorne}, hinten {hinten}")

vorne, hinten = teilen('abcd', 'xy')
print(f"Vorne: {vorne}, hinten {hinten}")

vorne, hinten = teilen('abcd', 'xy', 'aa')
print(f"Vorne: {vorne}, hinten {hinten}")
