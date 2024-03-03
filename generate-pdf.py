import requests
import os

key = os.environ['ILOVEPDF_API_TOKEN']

start = requests.get(' https://api.ilovepdf.com/v1/start/htmlpdf', headers={'Authorization': 'Bearer {key}'}).json()

print(start)
