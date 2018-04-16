# coding: utf-8
from api_client import ApiClient


class AppClient:

    def __init__(self, app_token):
        self.api_client = ApiClient(app_token)
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
