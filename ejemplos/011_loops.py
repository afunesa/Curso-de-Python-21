# WHILE
# FOR

# WHILE

a = 1
while a <= 100:
    print(f'a is {a}')
    a += 1

# FOR
text = 'hello world'
for character in text:
    print(character)

fruits = ['banana', 'apples', 'pears']

for fruit in fruits:
    print(fruit)

fruits = ['banana', 'apples', 'pears', 'orange']
a = 0
fruits_len = len(fruits)
while a < fruits_len:
    print('fruit is ', fruits[a])
    a += 1

fruits = {'banana', 'apples', 'pears', 'orange'}
for fruit in fruits:
    print(fruit)