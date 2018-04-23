# coding: utf-8
from api_client import ApiClient


class Calendar:

    def __init__(self, app_token):
        self.base = 'calendars'
        self.api_client = ApiClient(app_token, self.base)

    def create(self, resource_id, name, description, **kwargs):
        """
        required
        :param resource_id: string, id of the resource to create the calendar for
        :param name: string, name of calendar
        :param description: string, description of the calendar

        optional
        :param backgroundcolor: string, hex color to use as background for events
        :param foregroundcolor: string, hex color to use as forground for events

        returns new calendar object
        """
        data = kwargs

        data['resource_id'] = resource_id
        data['name'] = name
        data['description'] = description

        return self.api_client.call_api('post', data=data)

    def list(self):
        return self.api_client.call_api('get')

    def retrieve(self, calendar_id):
        """
        required
        :param calendar_id: string, id of calendar

        returns calendar object
        """
        url = self.base + '/' + str(calendar_id)

        return self.api_client.call_api('get', url)

    def update(self, calendar_id, **kwargs):
        """
        required
        :param calendar_id: string, id of calendar

        optional
        :param name: string, name of the calendar
        :param description: string, description of the calendar
        :param foregroundcolor: string, hex color code of the forground
        :param backgroundcolor: string, hex color code of the background
        :param provider_sync: boolean, enable or disable syncing
        :param primary: boolean, set the calendar as primary

        return boolean
        """
        url = self.base + '/' + str(calendar_id)
        data = kwargs

        return self.api_client.call_api('put', url, data)

    def delete(self, calendar_id):
        """
        required
        :param calendar_id: string, calendar id to delete

        returns boolean
        """
        url = self.base + '/' + str(calendar_id)
        return self.api_client.call_api('delete', url)
