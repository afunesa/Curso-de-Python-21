from aemet import Aemet, Estacion
import json


aemet_client = Aemet(api_key='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJmdW5lcy5hbG9uc29AZ21haWwuY29tIiwianRpIjoiMmFlMGE3ZWUtMzNmNi00YTY1LWFmZDEtZDg3MDZmNWVkNGY0IiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE2MTU0NTI5ODAsInVzZXJJZCI6IjJhZTBhN2VlLTMzZjYtNGE2NS1hZmQxLWQ4NzA2ZjVlZDRmNCIsInJvbGUiOiIifQ.mwiHWGu1W-z5mEcQlzzFtFxYUkFPyJAJG-i0whMfcHk')

print ('ok')

estaciones = Estacion.get_estaciones()[:3]

datos = []
anyo_inicio, anyo_fin = 2016, 2017 + 1

print(estaciones)
exit(0)

for estacion in estaciones:
    print('{}: {}'.format(estacion['indicativo'], estacion['nombre']))

    for anyo in range(anyo_inicio, anyo_fin):
        vcm = aemet.get_valores_climatologicos_mensuales(anyo, estacion['indicativo'])
        resultado = {
            'estacion': estacion,
            'valores_climatologicos': vcm,
            'anyo': anyo
        }
        datos.append(resultado)

print(json.dumps(datos, indent=2))