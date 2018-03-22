#!/usr/bin/python

import requests

URL='http://www.team%02d.isucdc.com'

for team in range(1, 20):
    team_url = URL % team
    print team_url
    payload = {'username': 'cdc', 'password': 'cdc'}
    resp = requests.post(url=team_url, data=payload)
    print resp.text


