seat_type = input("enter seat type(sleeper/AC/general/luxury)").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds are available")
    case "ac":
        print("Air conditioned, Comfy ride")
    case "general":
        print("chepest option, no reservation")
    case "luxury":
        print("premium seat with meals")
    case _:
        print("Invalid seat type")