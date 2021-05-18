import requests
import json

url = 'https://summerofcode.withgoogle.com/api/program/current/project/'

r = requests.get(url)
data = r.json()

name = []
org = []
project = []

data = data['results']

for item in data:
    name.append(item['student']['display_name'])
    org.append(item['organization']['name'])
    project.append(item['title'])
