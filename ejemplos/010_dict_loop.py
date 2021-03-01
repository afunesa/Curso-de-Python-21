person = {'name': 'Antonia', 'age': 28, 'location': 'Spain'}
second_person = {}
for key in person.keys():
    print(f'{key} -> {person[key]}')
    second_person[key] = person[key]

print(second_person)
second_person['name'] = 'Sonsoles'
print(second_person)
print(person)

person = {'name': 'Antonia', 'age': 28, 'location': 'Spain'}
second_person = {}

for key, value in person.items():
    second_person[key] = value

print(second_person)
second_person['name'] = 'Sonsoles'
print(second_person)
print(person)