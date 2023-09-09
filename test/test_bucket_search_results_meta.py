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
import datetime

import openbuckets
from openbuckets.models.bucket_search_results_meta import BucketSearchResultsMeta  # noqa: E501
from openbuckets.rest import ApiException

class TestBucketSearchResultsMeta(unittest.TestCase):
    """BucketSearchResultsMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BucketSearchResultsMeta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BucketSearchResultsMeta`
        """
        model = openbuckets.models.bucket_search_results_meta.BucketSearchResultsMeta()  # noqa: E501
        if include_optional :
            return BucketSearchResultsMeta(
                results = 56
            )
        else :
            return BucketSearchResultsMeta(
        )
        """

    def testBucketSearchResultsMeta(self):
        """Test BucketSearchResultsMeta"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
