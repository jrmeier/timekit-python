from api_client import ApiClient


class Credentials:

    def __init__(self, api_key):
        self.base = 'credentials'
        self.api_client = ApiClient(api_key)

    def widget(self):
        return self.api_client.call_api('get', url=self.base)

    def resource(self, resource_id):
        url = self.base + '?search=resource_id:'+str(resource_id)
        return self.api_client.call_api('get', url)
