flavours = ["Ginger", "out of stock", "Lemon","discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "out of stock":
        continue
    if flavour == "discontinued":
        break
    print(f"{flavour} item found")

print(f"out side of loop")