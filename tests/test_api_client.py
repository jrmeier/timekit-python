from timekit import ApiClient
import unittest
import json
import requests_mock


class TestApiClient(unittest.TestCase):
    """
    Test class for the API client
    """

    def setUp(self):
        self.client = ApiClient("test_token")

    @requests_mock.mock()
    def test_post(self, m):
        url = 'https://api.timekit.io/v2/invite'
        data = {'email': 'email@email.com'}
        m.post(url, json=data)
        self.assertTrue(self.client.call_api('post', url='invite', data=data))

    @requests_mock.mock()
    def test_get(self, m):
        url = 'https://api.timekit.io/v2/app'
        m.get(url)
        self.assertTrue(
            self.client.call_api('get', url='app'))

    @requests_mock.mock()
    def test_put(self, m):
        resource_id = '1111111-a2aa-3aaa-11a1-a11aaa1a1111'
        base_url = 'https://api.timekit.io/v2'
        mock_url = '{0}/resources/{1}'.format(base_url, resource_id)
        data = {
            'first_name': 'Mark',
            'last_name': 'Zuck'
        }
        m.put(mock_url, json=data)
        test_url = 'resources/{0}'.format(resource_id)

        self.assertTrue(self.client.call_api('put', url=test_url, data=data))


def suite():
    return unittest.TestLoader().loadTestsFromTestCase(TestApiClient)


if __name__ == "__main__":
    unittest.main()
