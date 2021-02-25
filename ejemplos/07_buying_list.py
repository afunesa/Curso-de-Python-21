# GIVEN A LIST WITH ITEMS
# GIVEN A LIST OF QUANTITY OF EACH ITEM
# when buy an element quit a numer in the element
# WHEN BUY ALL QUANTITY OF AN ITEM
# DELETE ITEM FROM THE LIST
# CONTINUE UNTIL THE LIST IS EMPTY

items = ['bananas', 'apples', 'eggs', 'bread', 'yogurt']
quantity = [3,          2,      6,      1,        4]

# buy banana
banana_position = items.index('bananas')
quantity[banana_position] = quantity[banana_position] - 1
print(quantity[banana_position])

# buy banana
quantity[banana_position] = quantity[banana_position] - 1
print(quantity[banana_position])

#buy banana
quantity[banana_position] = quantity[banana_position] - 1
print(quantity[banana_position])

items.remove('bananas')

print(items)



### BEST WAY

buying_list = [{'item': 'bananas', 'quantity': 3},
               {'item': 'apples', 'quantity': 2}]

# buy banana
banana = buying_list[0]['item']
quantity = buying_list[0]['quantity']

print('buying', banana)
print('quantity', quantity)
buying_list[0]['quantity'] = quantity - 1

banana =  buying_list[0]['item']
quantity = buying_list[0]['quantity']

print('buying', banana)
print('quantity', quantity)
buying_list[0]['quantity'] = quantity - 1

banana = buying_list[0]['item']
quantity = buying_list[0]['quantity']

print('buying', banana)
print('quantity', quantity)
