# coding: utf-8
import requests


class ApiClient(object):

    def __init__(self, app_token, api_url=None):
        self.headers = {'Content-Type': 'application/json'}
        self.auth = requests.auth.HTTPBasicAuth('', app_token)
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

        _type = _type.lower()
        if _type == 'post':
            data['fakingit'] = 'what'
            req = requests.post(
                url, json=data, headers=self.headers, auth=self.auth)

            if req.status_code in range(200, 206):
                try:
                    return req.json()
                except ValueError:
                    return True
            else:
                raise ApiException(
                    status=req.status_code,
                    reason=req.content
                )

        elif _type == 'get':
            if data:
                req = requests.get(url, headers=self.headers,
                                   auth=self.auth, params=data)
            else:
                req = requests.get(url, headers=self.headers, auth=self.auth)

            if req.status_code in range(200, 206):
                try:
                    return req.json()
                except ValueError:
                    return True
            else:
                raise ApiException(
                    status=req.status_code,
                    reason=req.content
                )
        elif _type == 'put':
            req = requests.put(
                url, json=data, headers=self.headers, auth=self.auth)

            if req.status_code in range(200, 206):
                return True
            else:
                raise ApiException(
                    status=req.status_code,
                    reason=req.content
                )
        elif _type == 'delete':
            req = requests.delete(
                url, json=data, headers=self.headers, auth=self.auth)

            if req.status_code == 200:
                return req.json()
            elif req.status_code == 204:
                return True
            else:
                raise ApiException(
                    status=req.status_code,
                    reason=req.content
                )
        else:
            return None


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        self.status = status
        self.reason = reason
        self.body = None
        self.headers = None

    def __str__(self):
        """
        Custom error messages for exception
        """
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
