# sets and frozenset
# everything in set is unique 

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

# union
all_spices = essential_spices | optional_spices
print(all_spices)

#intersection 
common_spices = essential_spices & optional_spices
print(common_spices)

# left join 
only_in_essential = essential_spices - optional_spices
print(only_in_essential)

#membership 
print('cloves' in optional_spices)

# frozenset are imuutable verison of set 
