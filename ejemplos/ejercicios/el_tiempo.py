import requests
from aemet import Aemet

#aemet_client = Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmdW5lcy5hbG9uc29AZ21haWwuY29tIiwianRpIjoiMmFlMGE3ZWUtMzNmNi00YTY1LWFmZDEtZDg3MDZmNWVkNGY0IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2MTU0NTI5ODAsInVzZXJJZCI6IjJhZTBhN2VlLTMzZjYtNGE2NS1hZmQxLWQ4NzA2ZjVlZDRmNCIsInJvbGUiOiIifQ.mwiHWGu1W-z5mEcQlzzFtFxYUkFPyJAJG-i0whMfcHk')

#aemet_client.descargar_mapa_rayos(rayos)

url = "https://opendata.aemet.es/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/"

querystring = {"api_key":"eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmdW5lcy5hbG9uc29AZ21haWwuY29tIiwianRpIjoiMmFlMGE3ZWUtMzNmNi00YTY1LWFmZDEtZDg3MDZmNWVkNGY0IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2MTU0NTI5ODAsInVzZXJJZCI6IjJhZTBhN2VlLTMzZjYtNGE2NS1hZmQxLWQ4NzA2ZjVlZDRmNCIsInJvbGUiOiIifQ.mwiHWGu1W-z5mEcQlzzFtFxYUkFPyJAJG-i0whMfcHk"}
headers = {
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(f'respuesta {response.text}')


BASE_URL = 'https://opendata.aemet.es/opendata/api'
MUNICIPIOS_DETALLE_API_URL = BASE_URL + '/maestro/municipio/{}'  # id






