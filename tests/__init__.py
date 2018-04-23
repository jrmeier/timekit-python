import unittest
import test_api_client


def suite():
    return unittest.TestSuite([
        test_api_client.suite()
    ])
