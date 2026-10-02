staff = [("adyy", 16), ("intel", 17), ("amd", 15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff")
        break
else:
    print("no one is eligible to manage the staff")