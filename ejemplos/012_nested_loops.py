# WHILE
# PRINT 2 TABLE


for number in range(1, 11):
    print(f'1 x {number} = {number}')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

for number in range(1, 11):
    print(f'2 x {number} = {2 * number}')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

for number in range(1, 11):
    print(f'3 x {number} = {3 * number}')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

for number in range(1, 11):
    print(f'4 x {number} = {4 * number}')


# REFACTORED
for number in range(1, 11):
    for multiplier in range(1, 11):
        print(f'{number} x {multiplier} = {number * multiplier}')
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')