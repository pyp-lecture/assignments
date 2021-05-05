FACTOR = 1.35962

def kW_to_PS(kw):
    return round(kw * FACTOR, 2)

def PS_to_kW(ps):
    return round(ps / FACTOR, 2)

print(kW_to_PS(146))
print(PS_to_kW(200))
