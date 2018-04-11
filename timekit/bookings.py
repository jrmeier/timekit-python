# coding: utf-8

import requests
import json

class Bookings(object):

    def __init__(self, api_key):
        self.url = 'https://api.timekit.io/v2/bookings'
        self.headers = {'Content-Type': 'application/json'}
        self.auth = requests.auth.HTTPBasicAuth('',api_key)
        self.api_key = api_key

    def create(self, **kwargs):
        """
        :query params
        :params includes: include booking attribute such as event_info in response
        
        :body params
        required
        :param resource_id: string, id of the resource being booked
        :param graph: string, name of flow graph you want to use, default is Comfirm_decline
        :param customer: object, customer info (depened on the chosen graph)
            :param customer.name: string
            :param customer.email: string
        :param start: string
        :param end: string
        :param what: string, title of the booking
        :param description: string, description of the booking
        :param where: stirng, description of the location of the booking

        optional
        :param customer.phone: string
        :param customer.voip: string
        :param customer.timezone: string
        :param settings: object
        :param calendar_id: string, id of the calendar, if its not primary
        :param meta: object, key-values of additonal custom metadata you want to save
        :param action: string, name of action that sould be triggered right after creation
        :param invite: boolean
        """

        data = kwargs

        if 'graph' not in kwargs.keys():
            data['graph'] = 'Confirm_decline'
        
        if 'settings' in kwargs.keys():
            data['settings'] = {'allow_double_bookings': kwargs['settings']}
        
        
