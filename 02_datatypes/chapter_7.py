# Tuples 
masala_spices = ("cardamom", "cloves", "cinnamon")
(spice1, spice2, spice3) = masala_spices
print(f"main masala spices: {spice1}, {spice2}, {spice3}")

ginger_ratio, cardamom_ratio = 2, 1
print(ginger_ratio, cardamom_ratio)
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
print(ginger_ratio, cardamom_ratio)

#membership testing (in keyword)
print(f"is giner in masala spices? {'ginger' in masala_spices}")