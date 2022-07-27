import os

import requests

BASE = 'https://cloud-api.yandex.net'
with open(os.getcwd() + '/token.txt', 'r') as f:
    TOKEN = f.readlines()[0]
PATH = '/free/trial'

def href_create(add='/v1/disk/resources'):
    res = BASE + add
    return res

def headers_create(token=TOKEN):
    res = {
    'Authorization': f'OAuth {token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}
    return res


def dir_create_YaDisk(path=PATH):
    resp = requests.put(href_create(),
                        headers=headers_create(),
                        params={
                            'path': path
                        })
    return resp