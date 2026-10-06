#pure function because it doesn't use any global variable
def pure_chai(cups):
    return cups * 10

total_chai = 0

# impure function because it is using a global function
def impure_chai(cups):
    global total_chai
    total_chai += cups

# recursive function 

def chai_poured(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return chai_poured(n-1)

print(chai_poured(10))

# lambda function 
chai_types = ["light", "kadak", "ginger", "kadak"]
strong_chai = list(filter(lambda chai: chai != "kadak", chai_types))
print(strong_chai)