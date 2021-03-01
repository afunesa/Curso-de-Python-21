# def say_jose():
#     print('HELLO MY NAME IS JOSE')
#
# def say_name(name):
#     print(f'Hello my name is {name}')
#
# say_jose()
# say_name('Desi')
#
# def multiply(a, b):
#     return a * b
#
# result = multiply(2, 8)
# print(result)

def multiply_small(a, b):
    result = a * b
    if result < 100:
        return result
    print('THIS IS BIGGER THAN 100')

x = multiply_small(2, 6)
print(x)
y = multiply_small(10,11)
print(y)