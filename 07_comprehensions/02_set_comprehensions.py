favorite_chai = [
    "masala chai", "green tea", "masala chai", "lemon tea", "green tea", "Elaichi chai"
]

unique_chai = {chai for chai in favorite_chai}
print(unique_chai)

recepies = {
    "masala chai": ["ginger", "cardamom", "clove"],
    "Elaichi chai": ["cardamom", "milk"],
    "spicy chai": ["ginger", "black pepper", "clove"]
}


unique_items = {spice for ingridients in recepies.values() for spice in ingridients}
print(unique_items)