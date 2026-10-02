# strings 
# strings are immutable 

chai_type = "Ginger Tea"
customer_name = "adyy"
print(f"order for {customer_name}: {chai_type} please!")

chai_description = "Aromatic and bold"
# indexing in string 
print({chai_description[0:8]})
print({chai_description[:8]}) # start from 0 ptint till 8th char 
print({chai_description[13:]}) # print after 13 char 
print({chai_description[0:8:2]}) # skip letter by 2 
print({chai_description[::-1]}) # print in reverse order
lable_text = "chai spécial"
encoded_label = lable_text.encode("utf-8")
print(encoded_label)
print(lable_text)
# A = 0, r = 1, o = 2, m = 3, a = 4, t = 5, i = 6, c = 7