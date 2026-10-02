value = 13
remainder = value % 5

if remainder:
    print(f"not divisible, remainder is {remainder}")

if (n := value % 5):
    print(f"not divisible, remainder is {n}")


avaiable_sizes = ["small", "medium", "large"]

if (requested_size := input("enter the size of cup: ")) in avaiable_sizes:
    print(f"you entered the cup size {requested_size}")
else:
    print("invalid cup size")