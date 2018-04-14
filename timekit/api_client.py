import requests

class ApiClient:

    def __init__(self, api_key):
        self.headers = {'Content-Type': 'application/json'}
        self.auth = requests.auth.HTTPBasicAuth('',api_key)
        self.base_url = 'https://api.timekit.io/v2/'

    def call_api(self, _type, url, data={}):
        url = self.base_url + url
        print url
        if _type == 'post':
            req = requests.post(url, json=data, headers=self.headers, auth=self.auth)
            if req.status_code == 200 or req.status_code == 201:
                return req.json()
            else:
                print req.content
                return None

        elif _type == 'get':
            req = requests.get(url, headers=self.headers, auth=self.auth)
            if req.status_code:
                return req.json()
            else:
                print req.content
                return None
        
        elif _type == 'put':
            req = requests.put(url, json=data, headers=self.headers, auth=self.auth)

            if req.status_code == 204:
                return True
            else:
                print req.content
                return None
        
        elif _type == 'delete':
            req = requests.delete(url, json=data, headers=self.headers, auth=self.auth)
            
            if req.status_code == 200:
                return req.json()
            elif req.status_code == 202 or req.status_code == 204:
                return True
            else:
                print req.content
                return False
        else:
            return None
