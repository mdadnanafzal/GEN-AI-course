chai_menu = {"masala":30, "ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("the key trying to access doesn't exist")

print("hello this is to check execution")
