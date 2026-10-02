# data types -> numbers -> integers, boolean, real (floating numbers), complex numbers

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams

print(f"total grams of base tea is {total_grams}")

remaning_tea = black_tea_grams - ginger_grams
print(f"total remaining tea is {remaning_tea}")

milk_litres = 7
serving = 4
milk_per_serving = milk_litres / serving
print(f"milk per serving is:{milk_per_serving}")

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"whole tea bags per pot: {bags_per_pot}")

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"letover c pods {leftover_pods}")

base_falvour_strength = 2
scale_factor = 3
powerfl_flavour = base_falvour_strength ** scale_factor
print(f"scaled flavour strenth {powerfl_flavour}")


total_tea_leaves_harvested = 1_000_000_000
print(total_tea_leaves_harvested)