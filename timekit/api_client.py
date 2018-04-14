import requests


class ApiClient:

    def __init__(self, api_key, api_url=None):
        self.headers = {'Content-Type': 'application/json'}
        self.auth = requests.auth.HTTPBasicAuth('', api_key)
        self.base_url = 'https://api.timekit.io/v2/'

        if api_url:
            self.api_url = api_url
        else:
            self.api_url = None

    def call_api(self, _type, url=None, data={}):
        if not url and self.api_url:
            url = self.base_url + self.api_url
        else:
            url = self.base_url + url

        if _type == 'post':
            req = requests.post(
                url, json=data, headers=self.headers, auth=self.auth)
            if req.status_code == 200 or req.status_code == 201:
                return req.json()
            else:
                print req.content
                return None

        elif _type == 'get':
            if data:
                req = requests.get(url, headers=self.headers,
                                   auth=self.auth, params=data)
            else:
                req = requests.get(url, headers=self.headers, auth=self.auth)
            if req.status_code:
                return req.json()
            else:
                print req.content
                return None

        elif _type == 'put':
            req = requests.put(
                url, json=data, headers=self.headers, auth=self.auth)

            if req.status_code == 204:
                return True
            else:
                print req.url
                print req.status_code
                print data
                print req.content
                return None

        elif _type == 'delete':
            req = requests.delete(
                url, json=data, headers=self.headers, auth=self.auth)

            if req.status_code == 200:
                return req.json()
            elif req.status_code == 202 or req.status_code == 204:
                return True
            else:
                print req.content
                return False
        else:
            return None
