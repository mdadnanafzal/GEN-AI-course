chai_type = "random_chai"
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type  # to acces the variable in the parent function 
        chai_type = "kesar"
    kitchen()
    print(f"after kitchen update what's the chai type {chai_type}")

update_order()
print(chai_type)