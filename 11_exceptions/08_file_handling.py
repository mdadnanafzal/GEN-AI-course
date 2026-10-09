# file = open("order.txt", "w")

# try:
#     file.write("Masala hai - 2 cups")
# finally:
#     file.close()

with open("orders.txt", "w") as file:
    file.write("ginger tea - 4 cups")
    