# chai = "Ginger chai"

# def prepare_chai(order):
#     print("preparing", order)


# prepare_chai(chai)
# print(chai)

chai = [1, 2, 3]
print(id(chai))
def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)
print(id(chai))