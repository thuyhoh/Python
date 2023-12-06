# dictionary = a changeable, unordered collection of unique key: value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {'Usa' : 'washing ton',
           'india' : 'new dehli',
           'russian': 'moscow' }
print(capitals)         # {"key":"value" ,....}
print(capitals.items()) # dict_items([ ('key','value'), (...), ... ])

# fuctions of dictionary
capitals.update({'germany':'berlin'})
capitals.update({'Usa':'new york'})
capitals.pop('russian')                 # remove russian from capitals

print(capitals['germany'])              # print the value have the key is germany
print(capitals.get('china'))            # print the value have the key is china if china isn't in capitals -> none
print(capitals.keys())                  # print all keys of capitals
print(capitals.values())                # print all values fo capitals

capitals.clear()  
