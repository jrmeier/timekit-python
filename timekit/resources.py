# coding: utf-8

import requests
import json
from tzlocal import get_localzone


class Resources(object):
    """
        explaination of wtf I'm doing
    """
    def __init__(self, api_key):
        self.url = "https://api.timekit.io/v2/resources"
        self.headers = {'Content-Type': 'application/json'}
        self.auth = requests.auth.HTTPBasicAuth('',api_key)
        self.api_key = api_key
    
    def list(self):
        req = requests.get(self.url, headers=self.headers, auth=self.auth)

        if req.status_code == 200:
            return req.json()
        else:
            return req

    
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


        req = requests.post(self.url, json=data, auth=self.auth)
        if req.status_code == 201:
            return req.json()
        else:
            return req
    
    def get(self, id):
        """
        :param id: id of resource
        """
        url = self.url + '/' +str(id)
        params = {'id': id}
        req = requests.get(url, params=params, headers=self.headers, auth=self.auth)

        if req.status_code == 200:
            return req.json()
        else:
            return req
    
    def update(self, id, **kwargs):
        """
        required
        :param id: id of the resource

        optional
        :parem name: string
        :param email: string
        :param first_name: string
        :param last_name: string
        :param password: string, if not set, a random password will be assigned
        :param timezone: timezone of the resource defaults to machine local
        """

        url = self.url + '/' + str(id)

        data = {
            'id': id
        }

        if 'name' in kwargs.keys():
            data['name'] = kwargs['name']

        if 'first_name' in kwargs.keys():
            data['first_name'] = kwargs['first_name']

        if 'last_name' in kwargs.keys():
            data['last_name'] = kwargs['last_name']

        if 'password' in kwargs.keys():
            data['password'] = kwargs['password']
        
        if len(data) <= 1:
            return False
        print "posting: ",data
        data = json.dumps(data)
        req = requests.put(url, headers=self.headers, auth=self.auth, data=data)

        if req.status_code == 204:
            return True
        else:
            return False
    
    def delete(self, id):
        url = self.url + '/' + str(id)
        req = requests.delete(url, headers=self.headers, auth=self.auth)
        if req.status_code == 204:
            return True
        else:
            return req





                