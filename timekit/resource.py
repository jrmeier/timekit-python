# coding: utf-8

from api_client import ApiClient
from tzlocal import get_localzone


class Resource:

    def __init__(self, api_key):
        self.base = "resources"
        self.api_client = ApiClient(api_key)

    def list(self):
        """
        returns an object of resources
        """
        return self.api_client.call_api('get', self.base)

    def create(self, name, timezone=None, email=None, first_name=None, last_name=None,
               password=None, tags=[]
               ):
        """
        required
        :param name: string, name of the resource
        :param timezone: timezone of the resource
            defaults to machine local

        optional
        :param email: string
        :param first_name: string
        :param last_name: string
        :param password: string, if not set, a random password will be assigned

        """
        if not timezone:
            timezone = get_localzone()

        data = {
            'name': name,
            'timezone': str(timezone)
        }
        if email:
            data['email'] = email

        if first_name:
            data['first_name'] = first_name

        if last_name:
            data['last_name'] = last_name

        if password:
            data['password'] = password

        return self.api_client.call_api('post', self.base, data)
        # req = requests.post(self.url, json=data, auth=self.auth)
        # if req.status_code == 201:
        #     return req.json()
        # else:
        #     return req

    def retrieve(self, resource_id):
        """
        :param resource_id: id of resource

        returns the resource object
        """
        url = self.base + '/' + str(resource_id)
        return self.api_client.call_api('get', url)

    def update(self, resource_id, **kwargs):
        """
        required
        :param resource_id: id of the resource

        optional
        :parem name: string
        :param first_name: string
        :param last_name: string
        :param password: string, if not set, a random password will be assigned
        :param timezone: timezone of the resource defaults to machine local
        """

        url = self.base + '/' + str(resource_id)

        data = kwargs
        data['id'] = str(resource_id)

        if len(data) <= 1:
            return False

        return self.api_client.call_api('put', url, kwargs)

    def delete(self, id):
        url = self.base + '/' + str(id)

        return self.api_client.call_api('delete', url)
