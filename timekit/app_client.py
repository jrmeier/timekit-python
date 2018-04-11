# coding: utf-8

import requests
import json

class AppClient(object):

    def __init__(self, api_key):
        self.base_url = "https://api.timekit.io/v2/app"
        self.headers = {'Content-Type': 'application/json'}
        self.auth = requests.auth.HTTPBasicAuth('',api_key)
        self.api_key = api_key

    def get_current_app(self):
        req = requests.get(self.base_url, auth=self.auth)
        if req.status_code == 200:
            return json.loads(req.content)
        else:
            return False
    
    def invite_resources(self, email):
        url = self.base_url + '/invite'
        print "url: ",url 
        data = {'email': email}
        data = json.dumps(data)
        req = requests.post(url, auth=self.auth, data=data, headers=self.headers)
        
        if req.status_code == 200:
            return json.loads(req.content)
        else:
            print "error: ",req.content 
        return 
    