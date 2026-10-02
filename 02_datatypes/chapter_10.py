chai_order = dict(type="masala chai", size = "large", sugar = 2)
print(chai_order)

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(chai_recipe['base'])
print(chai_recipe)

del chai_recipe["liquid"]
print(chai_recipe)

#membership
print('sugar' in chai_order)

print(f"order details (keys): {chai_order.keys()}")
print(f"order details (values): {chai_order.values()}")
print(f"order details (items): {chai_order.items()}")
