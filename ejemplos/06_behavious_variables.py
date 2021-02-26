# POINTERS

PI = 3.14
print('pi', PI)
PI = 3
print('changed pi', PI)

first_number = 1
second_number = first_number + 1
print(first_number)
print(second_number)

first_letter = 'h'
second_letter = first_letter # 'h'
second_letter = 'hola'
print(first_letter)
print(second_letter)

numbers = [1, 2]
more_numbers = numbers
third_numbers = more_numbers
more_and_more_numbers = third_numbers
more_numbers.append(3)
print(numbers)
print(more_numbers)
print(third_numbers)
print(more_and_more_numbers)
more_and_more_numbers.pop()
print(numbers)
print(more_numbers)
print(third_numbers)
print(more_and_more_numbers)

carlos = {'name': 'Carlos', 'company': 'Envera'}
laura = carlos
laura['name'] = 'Laura'
print(carlos)
print(laura)
carlos['surname'] = 'Alvez'
print(carlos)
print(laura)


# COPIES
FIRST_LIST = [1, 2, 3]
second_list = FIRST_LIST[:]
second_list.pop()
print(FIRST_LIST)
print(second_list)


carlos = {'name': 'Carlos', 'company': 'Envera', 'age': 10}
laura = dict()
#copy
laura['company'] = carlos['company']
laura['age'] = carlos['age']
laura['name'] = carlos['name']
#change
laura['name'] = 'Laura'
print(carlos)
print(laura)
carlos['surname'] = 'Alvez'
print(carlos)
print(laura)


