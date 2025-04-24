first_place = "Alice"
second_place = "Bob"
third_place = "Charlie"
fourth_place = "Dana"
fifth_place = "Eli"

print("🏁 Race Results:")
print("1st Place:", first_place)
print("2nd Place:", second_place)
print("3rd Place:", third_place)
print("4th Place:", fourth_place)
print("5th Place:", fifth_place)


places = []

for i in range(1, 1001):
    places.append(f"Runner{i}")

# Example: print top 5
for i in range(5):
    print(f"{i+1}st Place: {places[i]}")
