order_amount = int(input("Enter the order amount: "))
delivery_fees = 0 if order_amount > 300 else 30

# print(f"Order amount: {type(order_amount)}")
print(delivery_fees)