import pandas as pd
import requests

url = 'https://summerofcode.withgoogle.com/api/program/current/project/'

name = []
org = []
project = []

i = 1
while(True):
    params = {'page': i}
    r = requests.get(url, params)
    data = r.json()
    data = data['results']
    if len(data) == 0:
        break
    for item in data:
        name.append(item['student']['display_name'])
        org.append(item['organization']['name'])
        project.append(item['title'])
    i += 1

dict = {'Name': name, 'Organization': org, 'Project': project}
df = pd.DataFrame(dict)

df.to_csv('gsoc2021.csv', index = False)
