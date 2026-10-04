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

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "yes", "low")
make_chai(tea="Green", sugar="medium", milk="no")


def special_chai(*ingredients, **extras): # args, *kwargs
    print("Ingridients", ingredients)
    print("Extras", extras)

special_chai("cinnamon", "cardamom", sweetner = "Honey", foam = "yes")