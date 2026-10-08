class Chai:
    temperature = "hot"
    strength = "strong"

cutting_chai = Chai()
print(cutting_chai.temperature)

cutting_chai.temperature = "Mild"
cutting_chai.cup = "small"
print("After chaging: ", cutting_chai.temperature)
print("cup size is: ", cutting_chai.cup)
print("direct look into the class: ", Chai.temperature)

del cutting_chai.temperature
del cutting_chai.cup
print("after deleting checking the value", cutting_chai.temperature)
print("after deleting the value for cup size which is not the attribute in original class:", cutting_chai.cup)
# This will give error AttributeError: 'Chai' object has no attribute 'cup' because there is no fall back
# attribute shadowing -> when the object created for a class is deleted then it's value falls back to value which is there in class