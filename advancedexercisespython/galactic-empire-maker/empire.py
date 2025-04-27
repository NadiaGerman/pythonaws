# Galactic Empire Maker - Build your own star empire!

# Ask the user for their empire name
empire_name = input("Enter the name of your Galactic Empire: ")

# Ask how many planets to conquer
planet_count = int(input("How many planets will your empire rule? "))

# Collect planet names
planets = []
for i in range(planet_count):
    planet = input(f"Enter the name of planet #{i+1}: ")
    planets.append(planet)

# Ask for ruler name and fleet strength
ruler_name = input("Enter the name of your supreme ruler: ")
fleet_strength = int(input("Enter your fleet strength (1-100): "))

# Show empire summary
print("\n--- Empire Summary ---")
print(f"Empire Name: {empire_name}")
print(f"Ruler: {ruler_name}")
print(f"Number of Planets: {len(planets)}")
print(f"Fleet Strength: {fleet_strength}/100")
print("Conquered Planets:")
for p in planets:
    print(f"- {p}")

# Empire rating
if fleet_strength > 80:
    print("Your empire is feared across the galaxy!")
elif fleet_strength > 50:
    print("Your empire is strong but has room to grow.")
else:
    print("Your empire is vulnerable. Strengthen your forces!")
