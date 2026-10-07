def chai_customer():
    print("welcome! what chai would you like ?")
    order = yield
    while True:
        print(f"preparing: {order}")
        order = yield

stall = chai_customer()
next(stall) # starting the generators
stall.send("Masala chai")
stall.send("Lemon chai")