cup_size =  input("choose your cup size(small/medium/large)").lower()

if cup_size == "small":
    print("price is Rs.10")
elif cup_size == "medium":
    print("price is Rs.15")
elif cup_size == 'large':
    print("price is Rs.20")
else:
    print("Unknown cup size")
