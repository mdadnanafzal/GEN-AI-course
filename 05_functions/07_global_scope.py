chai_type = "plain"

def front_desk():
    def kitchen():
        global chai_type  # to access the  variable which is gl0bally present in the code
        chai_type = "Irani"
    kitchen()

front_desk()
print(f"final global chai: {chai_type}")