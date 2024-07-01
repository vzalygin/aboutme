import requests
import os

key = os.environ['ILOVEPDF_API_KEY']

start = requests.get('https://api.ilovepdf.com/v1/start/htmlpdf', headers={'Authorization': f'Bearer {key}'}).json()

print(start)
