# coding: utf-8
from api_client import ApiClient

class AppClient:

    def __init__(self, api_key):
        self.api_client = ApiClient(api_key)
        self.base = 'app'

    def get_current_app(self):
        """
        returns the application object
        """

        return self.api_client.call_api('get', self.base)
    
    def invite_resources(self, email):
        """
        required
        :param email: string, email address to invite
        
        returns: the new resource object
        """
        url = self.base + '/invite'
        data = {'email': email}
        return self.api_client.call_api('post', url, data=data)
