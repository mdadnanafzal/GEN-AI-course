tea_prices_int = {
    "masala chai": 40, 
    "green tea": 50, 
    "lemon tea":200
}

tea_prices = {tea:price for tea, price in tea_prices_int.items()}
print(tea_prices)

tea_prices_check = { tea for tea in tea_prices.values() for price in tea}
print(tea_prices_check)