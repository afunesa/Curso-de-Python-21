# call to random starwars api people
# name of the person
import requests
import xlsxwriter

filepath = './persistence/starwars.xlsx'
workbook = xlsxwriter.Workbook(filepath)
worksheet = workbook.add_worksheet('person_info')

MAX_PERSON_ID = 3

people_info = []
for number in range(1, MAX_PERSON_ID):
    print(f'requesting data for person {number}')
    person = requests.get(f'https://swapi.dev/api/people/{number}/')
    person_data = person.json()
    person_info = {'name': person_data.get('name'), 'films': []}
    films = person_data.get('films', [])

    for film in films:
        film = requests.get(f'{film}')
        film = film.json()
        person_info['films'].append({'title': film.get('title'), 'episode': film.get('episode_id', 0)})

    people_info.append(person_info)

print(people_info)

headers = ['name', 'films']
for index, header in enumerate(headers):
    worksheet.write(0, index, header)

for row, person_detail in enumerate(people_info, start=1):
    #row, fila
    #col, columna
    print(person_detail)
    worksheet.write(row, 0, person_detail.get('name'))
    worksheet.write(row, 1, str(person_detail.get('films')))

workbook.close()