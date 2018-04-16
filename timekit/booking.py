# coding: utf-8

from api_client import ApiClient
from to_rfc3339 import to_rfc3339


class Booking:

    def __init__(self, app_token):
        self.api_client = ApiClient(app_token)
        self.base = 'bookings'

    def create(self, *args, **kwargs):
        """
        :query params
        :params includes: include booking attribute such as event_info in response

        :body params
        required
        :param resource_id: string, id of the resource being booked
        :param customer: object, customer info (depened on the chosen graph)
            :param customer.name: string
            :param customer.email: string
        :param start: datetime object
        :param end: datetime object
        :param what: string, title of the booking
        :param description: string, description of the booking
        :param where: stirng, description of the location of the booking

        optional
        :param graph: string, name of flow graph you want to use, default is Comfirm_decline
        :param customer.phone: string
        :param customer.voip: string
        :param customer.timezone: string
        :param settings: object
        :param calendar_id: string, id of the calendar, if its not primary
        :param meta: object, key-values of additonal custom metadata you want to save
        :param action: string, name of action that sould be triggered right after creation
        :param invite: boolean
        """

        if kwargs:
            data = kwargs
        else:
            data = args[0]

        if 'graph' not in kwargs.keys():
            data['graph'] = 'confirm_decline'

        if 'settings' in kwargs.keys():
            data['settings'] = {'allow_double_bookings': kwargs['settings']}

        if 'action' not in kwargs.keys():
            data['action'] = 'create'
        data['start'] = to_rfc3339(data['start'])
        data['end'] = to_rfc3339(data['end'])

        return self.api_client.call_api('post', self.base, data)

    def list(self, **kwargs):
        """
        :param limit: int32, pagination limit intervals (x means first x is returned)
        :param page: int32, which pagination interval to retrieve (set limit for interval size)
        :param search: string, add 1 or more search criteria
        :param include: string, dynamic includes
        :param orderBy: dict/strings: created_at, updated_at, completed, graph, state
                        dict: event{start, end}
        :param sortedBy: string, asc, desc
        :param start: datetime object
        :param end: datetime object
        """
        data = kwargs
        if 'start' in kwargs:
            data['start'] = to_rfc3339(data['start'])

        if 'end' in kwargs:
            data['end'] = to_rfc3339(data['end'])

        url = "?search="
        for key in data:
            url += key + ':'+data[key] + '&'

        url = url[:-1]

        return self.api_client.call_api('get', url=url)

    def retrieve(self, booking_id, includes=[]):
        """
        required
        :params booking_id: string

        optional
        :param includes: array of strings of dynamic includes

        returns
        object of booking_id
        """

        url = self.base + '/' + booking_id
        return self.api_client.call_api('get', url=url)

    def confirm(self, booking_id):
        """
        required
        :param booking_id: string, id of the booking to cancel

        returns: object of the booking confirmed
        """

        return self._update_state(booking_id, 'confirm')

    def decline(self, booking_id):
        """
        required
        :param booking_id: string, id of booking to decline

        returns: object of the declined booking
        """

        return self._update_state(booking_id, 'decline')

    def cancel(self, booking_id):
        """
        required
        :param booking_id: string, booking to cancel

        returns: object of the canceled booking
        """

        return self._update_state(booking_id, 'cancel')

    def _update_state(self, booking_id, action):
        """
        required
        :params id: string
        :params action: string, which action to trigger
        """
        url = self.base + '/' + booking_id + '/' + action

        return self.api_client.call_api('put', url=url)
