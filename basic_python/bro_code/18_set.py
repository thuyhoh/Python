# set = colletion which is unordered, unindexed. No duplicate values

utensils = {"fork","spoon","knife","spoon","knife"}
print(utensils) # spoon and knife appear one time

dishes = {"bowl","plate","cup","knife"}

utensils.add("napkin") # add the "napkin" into the set
utensils.remove("fork") # remove "fork" from the set
dishes.update(utensils) # dishes = dishes + utensils 
dinner_table = utensils.union(dishes) # dinner = utensils + dishes

print(dishes.difference(utensils))   # different betwen dishes and utensils
print(utensils.intersection(dishes)) # common betwen utensils and dishes

