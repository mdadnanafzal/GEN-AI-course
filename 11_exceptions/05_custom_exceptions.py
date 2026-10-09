def brew_chai(flavor):
     if flavor not in ["masala", "ginger", "elaichi"]:
        raise ValueError("unsuppoted chai flavor...")
        print(f"brewign {flavor} chai...")

brew_chai("mint")