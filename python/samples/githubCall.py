import sys
import requests
import json
import yaml

repo = ""
username = ""
token = ""

def setup():
    global projectName, repo, token
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        repo = cfg['github']['repo']
        organization = cfg['github']['organization']
        username = cfg['github']['username']
        token = cfg['github']['token']

def findPR():
    url = 'https://api.github.com/repos/'+repo+'/commits'
    r = requests.get(url, auth=(username,token))
    json_data = json.loads(r.text)
    print json_data
    return json_data


if __name__ == "__main__":
    test()
