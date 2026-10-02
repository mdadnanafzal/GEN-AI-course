# list, array -> mutable 
# ingridients = ["water", "milk", "black_tea"]
# ingridients.append("sugar")
# print(ingridients)
# ingridients.remove("water")
# print(ingridients)

spice_ingredients = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_ingredients)
print(chai_ingredients)

chai_ingredients.insert(2, "black tea")
print(chai_ingredients)

last_added =  chai_ingredients.pop()
print(last_added)

chai_ingredients.reverse()
print(chai_ingredients)

chai_ingredients.sort()
print(chai_ingredients)


sugar_level = [1, 2, 3, 4, 5, 6]
print(f"max of sugar level is: {max(sugar_level)}")
print(f"max of sugar level is: {min(sugar_level)}")

# operator overloading 
base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]
full_liquid_mix = base_liquid + extra_flavour
print(full_liquid_mix)

strong_brew = ["black tea", "water"] * 3
print(strong_brew)

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(raw_spice_data)