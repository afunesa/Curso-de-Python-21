import requests
import xlsxwriter

filepath = './persistence/el_tiempo.xlsx'
workbook = xlsxwriter.Workbook(filepath)
worksheet = workbook.add_worksheet('info')



wheather_info = []

r = requests.get("https://dev.twitter.com/docs/api/1.1/overview")
if r.status_code == 200:
    print(r.status_code)

print(r.status_code)
print(r.text)