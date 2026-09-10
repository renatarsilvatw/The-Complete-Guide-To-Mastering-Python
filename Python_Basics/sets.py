items: set = {'apple', 'banana', 10, True, True, 'apple'}
items2: set = {'Watermelon', 'pumpkin', 'banana'}

items.update(['orange', 15])

# print(items)
# items.clear() ## limpar todos os items

# print(len(items))

new_items = items.union(items2) #só mantem um se um item tiver duplicado
print(new_items)

items.intersection_update(items2) #traz items duplicados
print(items)

new_set = items.symmetric_difference(items2) #traz items nao duplicados
print(new_set)
