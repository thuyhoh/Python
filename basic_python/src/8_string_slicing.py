# slicig = create a sub by extacting emlement from another string
#          indexing[] or slice()
#          [start:stop:step]


# indexing[]
name = "nguyen trong thuy"
first_name = name[0:6] # name[0] -> name[5]
print(first_name)

last_name = name[7:17] # name[0] -> name[16]
print(last_name)

funky_name = name[::3] # ny o u
print(funky_name)

reversed_name = name[::-1] # yuht gnort neyugn
print(reversed_name)

# slice()
website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) # remove "http://"(0->6) and ".com"(-3 -> 0)
print(website1[slice])
print(website2[slice])