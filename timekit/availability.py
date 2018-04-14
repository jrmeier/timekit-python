from api_client import ApiClient
from to_rfc3339 import to_rfc3339

class Availability:

    def __init__(self, api_key):
        self.base = 'findtime'
        self.api_client = ApiClient(api_key)
    
    def query(self, resource_ids, **kwargs):
        """
        Required
        Note: only resource_ids or calendar_ids are required
        :param resource_ids: array, resource-uuids
        :param: calendar_ids: array of strings, use this for only specific calendars

        Optional:
        :param length: string, how much time must each avaliable timeslot contain
        :param filters: array (mixed types, see filters)
        :param start: string, human written time eg, 1 day, tomorrow, 2 weeks
        :param future: string, defines the end of the search-space
        :param sort: string, chronologica order of results, accepted values: asc, desc
        :param ignore_all_day_events: boolean, ignore all day events in this query?
        :param all_solutions: boolean, return overlapping timeslots?
        :param emails: array of strings, check emails for mutual availability
        :param buffer: string, amount of time to add to each booking
        :param no_day_span: boolean, if you dont want time-slots that span span days
        """

        data = kwargs

        if type(resource_ids) == str:
            data['resource_ids'] = [resource_ids]
        

            
        return self.api_client.call_api('post',self.base, data)





        