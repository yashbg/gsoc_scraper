import pandas as pd
import requests

url = 'https://summerofcode.withgoogle.com/api/program/current/project/'

names = []
orgs = []
projects = []

i = 1
while True:
    params = {'page': i}
    r = requests.get(url, params)
    data = r.json()
    data = data['results']
    if len(data) == 0:
        break
    for item in data:
        names.append(item['student']['display_name'])
        orgs.append(item['organization']['name'])
        projects.append(item['title'])
    i += 1

dict = {'Name': names, 'Organization': orgs, 'Project': projects}
df = pd.DataFrame(dict)

df.to_csv('gsoc2021.csv', index = False)
