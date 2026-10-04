users = [
    {"id":1, "total":100, "cupon":"P20"},
    {"id":2, "total":150, "cupon":"F10"},
    {"id":3, "total":80, "cupon":"P50"}
]

discounts = {
    "P20":(0.2,0),
    "F10":(0.5,0),
    "P50":(0,10)
}

for user in users:
    percent, fixed = discounts.get(user["cupon"], (0,0))
    discount = user["total"] * percent + fixed
    print(f" user {user["id"]} paid {user["total"]} and got discount for next visit for {discount}")

