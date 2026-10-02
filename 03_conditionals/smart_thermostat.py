device_status = "inactive"
temperature = 34

if device_status == "active":
    if temperature > 35:
        print("High temperature Alert!")
    else:
        print("Normal Temperature")
else:
    print("device is offline")