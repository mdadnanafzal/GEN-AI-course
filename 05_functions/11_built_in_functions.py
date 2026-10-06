def chai_flavor(flavor = "masala"):
    """return the flavor of chai."""
    return flavor

print(chai_flavor.__doc__) # prints the document of the function 
print(chai_flavor.__name__) # returns the name of the function 
help(len)


def generate_bill(chai = 0, samosa = 0):
    """
    calculate the total bill for chai and samosa 
    :param chai: number of chai cups(10 rupees each)
    : param samosa: number of  samosa(15 rupes each)
    : return (total amount, thank you message as a string)
    """
    total = chai * 10 + samosa *15
    return total, "thank you visiting adyy.com"

print(generate_bill.__doc__)

