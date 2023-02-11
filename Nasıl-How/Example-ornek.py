import requests
from bs4 import BeautifulSoup
import json
URL = "https://deprem-api-delta.vercel.app/tum"
response = requests.get(URL)
a = response.json()
print(a)
