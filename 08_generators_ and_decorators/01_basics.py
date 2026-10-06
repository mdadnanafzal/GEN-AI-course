# # generators basics 

# def serve_chai():
#     yield "cup 1: Masala chai"
#     yield "cup 2: Ginger chai"
#     yield "cup 3: Elaichi chai"

# stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["cup1", "cup2", "cup3"]

def get_chai_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"

answer = get_chai_gen()
print(answer) # this will only print the address of the memory location where the values are stored

print(next(answer)) # this will only print the first yield value 
print(next(answer)) # this will print only the seconf yield value becuase it will pause the function call when it was called first 
print(next(answer)) # this will print only the third yield value becuse it will resume from the last yield value
