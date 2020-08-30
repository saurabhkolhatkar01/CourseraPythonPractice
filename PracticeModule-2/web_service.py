#!/usr/bin/env python3
import os
import requests

BASEPATH = '/reviews/'
folder = os.listdir(BASEPATH)
list = []
for file in folder:
    with open(BASEPATH + file, 'r') as f:
        list.append({
            "title": f.readline().rstrip("\n"),
            "name": f.readline().rstrip("\n"),
            "date": f.readline().rstrip("\n"),
            "feedback": f.read().rstrip("\n")
        })

for item in list:
    resp = requests.post("http://34.72.8.98/feedback/", json=item)
    if resp.status_code != 201:
        raise Exception('POST error status={}'.format(resp.status_code))
    print('Created Feedback ID: {}'.format(resp.json()["id"]))
