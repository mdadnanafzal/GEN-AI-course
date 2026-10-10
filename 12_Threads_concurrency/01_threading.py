import threading
import time 

def take_orders():
    for i in range(1, 4):
        print(f"taking order for #{i}")
        time.sleep(1)
    
def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}")
        time.sleep(2)
    
#create theads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start() 
brew_thread.start()
# two threads running two different functions in the same process -> multithreading

# wait for both to finish 

order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed")