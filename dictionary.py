#Dictionary (Hash Map, key: value, JSON)

fruits = {'orange':400, 'apple':200, 'banna':100}
print(fruits.keys())
print(fruits.values())
print(int(500) in fruits.values())

for key, val in fruits.items():
    print(key,' ', val)