def energy(mass):
    return mass * (300000000) ** 2

mass = float(input("Write the mass (in kilograms): "))

print(f"The energy of this mass will be: {energy(mass)/1000}KJ")