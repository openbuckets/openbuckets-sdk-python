# coding: utf-8

"""
    OpenBuckets API

    The OpenBuckets web-based tool is a powerful utility that allows users to quickly locate open buckets in cloud storage systems through a simple query. In addition, it provides a convenient way to search for various file types across these open buckets, making it an essential tool for security professionals, researchers, and anyone interested in discovering exposed data. This Postman collection aims to showcase the capabilities of OpenBuckets by providing a set of API requests that demonstrate how to leverage its features. By following this collection, you'll learn how to utilize OpenBuckets to identify open buckets and search for specific file types within them.

    The version of the OpenAPI document: 1.0.0
    Contact: support@openbuckets.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import openbuckets
from openbuckets.api.buckets_api import BucketsApi  # noqa: E501
from openbuckets.rest import ApiException


class TestBucketsApi(unittest.TestCase):
    """BucketsApi unit test stubs"""

    def setUp(self):
        self.api = openbuckets.api.buckets_api.BucketsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_search_buckets(self):
        """Test case for search_buckets

        Search Buckets  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
