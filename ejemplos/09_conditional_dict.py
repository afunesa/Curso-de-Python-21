# DISCO
# GIVEN A CLIENT WITH AN AGE
# GIVEN A COUNTRY
# CLIENT GO TO THE DISCO
# SECURITY GUARD ALLOW ACCESS IF IS ALLOWED IN HIS COUNTRY

# country_text = '''
# Choose one number:
# 1.- Spain
# 2.- France
# 3.- EEUU
# '''



# client_age = input('Tell me your age: ')
# try:
#     client_age = int(client_age)
# except ValueError as err:
#     client_age = 18
#     print(f'WE HAVE AN ERROR {err}, so we put client_age age as {client_age}')
#
# print(country_text)
# country_number = int(input('Choose a country number: '))
# if country_number <= 0 or country_number > 3:
#     print('PLEASE SELECT A VALID NUMBER')
#     raise Exception
#
# if country_number == 1:
#     age = 18
#     print(f'YOU ARE IN SPAIN AND THE AGE IS {age}')
#     if client_age >= age:
#         print('PLEASE COME IN')
#     else:
#         print('YOU SHALL NOT PASS')
# elif country_number == 2:
#     age = 19
#     print(f'YOU ARE IN FRANCE AND THE AGE IS {age}')
#     if client_age >= age:
#         print('PLEASE COME IN')
#     else:
#         print('YOU SHALL NOT PASS')
# else:
#     age = 21
#     print(f'YOU ARE IN EEUU AND THE AGE IS {age}')
#     if client_age >= age:
#         print('PLEASE COME IN')
#     else:
#         print('YOU SHALL NOT PASS')

# REFACTOR
#
# country_text = '''
# Choose one number:
# 1.- Spain
# 2.- France
# 3.- EEUU
# '''
#
# COUNTRIES_RULES = {
#                    1: {'name': 'Spain', 'age': 18},
#                    2: {'name': 'France', 'age': 19},
#                    3: {'name': 'EEUU', 'age': 21}
#                    }
#
# client_age = input('Tell me your age: ')
# try:
#     client_age = int(client_age)
# except ValueError as err:
#     client_age = 18
#     print(f'WE HAVE AN ERROR {err}, so we put client_age age as {client_age}')
#
# print(country_text)
# country_number = int(input('Choose a country number: '))
# country = COUNTRIES_RULES[country_number]
# print(f'YOU ARE IN {country["name"]} AND THE AGE IS {country["age"]}')
# if client_age >= country["age"]:
#     print('PLEASE COME IN')
# else:
#     print('YOU SHALL NOT PASS')
#

fruits = ['bananas', 'apples', 'pears', 'oranges']
count = 0
num_items = len(fruits)
print(num_items)

while count <= (num_items-1):
    print (fruits[count])
    count = count + 1
