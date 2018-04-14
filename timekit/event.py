# coding utf-8

from api_client import ApiClient
from to_rfc3339 import to_rfc3339


class Event:

    def __init__(self, api_key):
        self.base = 'events'
        self.api_client = ApiClient(api_key, self.base)

    def create(self, start, end, what, where, calendar_id, resource_id, **kwargs):
        """
        required
        :param start: datetime, start of the event
        :param end: datetime, end of the event
        :param what: string, description of the event
        :param where: string, location of the event
        :param calendar_id: string, calendar to add the event to
        :param resource_id: string, resources_id

        optional
        :param participants: array of strings, eamils to invite as participants
        :param invite: boolean
        :param description: string, description of the event
        :param my_rsvp: string, allowed values: accepted, needsAction, declined, tentative
        :param sync_provider: boolean, triggers a sync with the provider
        :param all_day: boolean, if true, date will be sent to google as an all day event
        """
        data = kwargs

        data['start'] = to_rfc3339(start)
        data['end'] = to_rfc3339(end)
        data['what'] = what
        data['where'] = where
        data['calendar_id'] = calendar_id

        return self.api_client.call_api('post', data=data)

    def list(self, start, end, search=None):
        """
        required
        :param start: datetime, of start time
        :param end: datetime, of end time,

        optional
        :param search: sring, only allowd value is resource id

        returns a list meeting these critera
        """

        data = {
            'start': to_rfc3339(start),
            'end': to_rfc3339(end)
        }

        if search:
            data['search'] = "?resource_id:"+search

        print "data from list: ", data
        return self.api_client.call_api('get', data=data)

    def retrieve(self, event_id):
        """
        required
        :param event_id: id of the event

        return the event object
        """

        url = self.base + '/' + str(event_id)
        return self.api_client.call_api('get', url)

    def update(self, event_id, **kwargs):
        """
        required
        :param event_id: string, id of the event

        optional
        :param start: datetime, start time of the event
        :param end: datetime, end of the event
        :param what: string, name of the event
        :param where: string, where the event is taking place
        :param participates: array of strings, emails to invite
        :param all_day: boolean, is this an all day event?
        """
        url = self.base + '/' + str(event_id)
        data = kwargs
        if 'start' in data:
            data['start'] = to_rfc3339(data['start'])

        if 'end' in data:
            data['end'] = to_rfc3339(data['end'])
        return self.api_client.call_api('put', url, data=data)

    def delete(self, event_id):
        """
        required
        :param event_id: string, id of event to delete

        return boolean
        """
        url = self.base + '/' + str(event_id)
        return self.api_client.call_api('delete', url)
