def serve_chai(flavor):
    try:
        print(f"preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("we don't have that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("next customer please")
    
serve_chai("masala ")
serve_chai("unknown")