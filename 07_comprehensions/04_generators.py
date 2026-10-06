"""
[x for x in items] -> make entire list in memory
(x for x in items) -> make a stream 
"""

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

# total_cups = [sale for sale in daily_sales if sale > 5]
total_cups = sum(sale for sale in daily_sales if sale > 5) # generators

print(total_cups)