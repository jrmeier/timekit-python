# coding: utf-8
from api_client import ApiClient


class Credentials:

    def __init__(self, app_token):
        self.base = 'credentials'
        self.api_client = ApiClient(app_token)

    def widget(self):
        return self.api_client.call_api('get', url=self.base)

    def resource(self, resource_id):
        url = self.base + '?search=resource_id:'+str(resource_id)
        return self.api_client.call_api('get', url)
