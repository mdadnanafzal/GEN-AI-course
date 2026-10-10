import threading
import time 

def boil_milk():
    print(f"boiling milk...")
    time.sleep(2)
    print(f"milk boiled...")

def toast_bun():
    print("toasting bun...")
    time.sleep(2)
    print("toasting bun is done...")

start = time.time()

t1 = threading.Thread(target = boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print(f"breakfas is ready in {end - start:.2f} seconds")