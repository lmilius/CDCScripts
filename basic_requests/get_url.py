#!/usr/bin/python

import requests

URL='http://www.team%02d.isucdc.com'

for team in range(1, 20):
    team_url = URL % team
    print team_url
    resp = requests.get(team_url)
    print resp.text


