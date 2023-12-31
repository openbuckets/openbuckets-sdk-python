# coding: utf-8

"""
    OpenBuckets API

    The OpenBuckets web-based tool is a powerful utility that allows users to quickly locate open buckets in cloud storage systems through a simple query. In addition, it provides a convenient way to search for various file types across these open buckets, making it an essential tool for security professionals, researchers, and anyone interested in discovering exposed data. This Postman collection aims to showcase the capabilities of OpenBuckets by providing a set of API requests that demonstrate how to leverage its features. By following this collection, you'll learn how to utilize OpenBuckets to identify open buckets and search for specific file types within them.

    The version of the OpenAPI document: 1.0.0
    Contact: support@openbuckets.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, conlist
from openbuckets.models.bucket_search_results_buckets_inner import BucketSearchResultsBucketsInner
from openbuckets.models.bucket_search_results_meta import BucketSearchResultsMeta
from openbuckets.models.bucket_search_results_query import BucketSearchResultsQuery

class BucketSearchResults(BaseModel):
    """
    The search results for buckets.
    """
    buckets: Optional[conlist(BucketSearchResultsBucketsInner)] = Field(None, description="An array of buckets.")
    meta: Optional[BucketSearchResultsMeta] = None
    query: Optional[BucketSearchResultsQuery] = None
    __properties = ["buckets", "meta", "query"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> BucketSearchResults:
        """Create an instance of BucketSearchResults from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in buckets (list)
        _items = []
        if self.buckets:
            for _item in self.buckets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['buckets'] = _items
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of query
        if self.query:
            _dict['query'] = self.query.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BucketSearchResults:
        """Create an instance of BucketSearchResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BucketSearchResults.parse_obj(obj)

        _obj = BucketSearchResults.parse_obj({
            "buckets": [BucketSearchResultsBucketsInner.from_dict(_item) for _item in obj.get("buckets")] if obj.get("buckets") is not None else None,
            "meta": BucketSearchResultsMeta.from_dict(obj.get("meta")) if obj.get("meta") is not None else None,
            "query": BucketSearchResultsQuery.from_dict(obj.get("query")) if obj.get("query") is not None else None
        })
        return _obj


