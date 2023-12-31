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


from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr

class File(BaseModel):
    """
    File
    """
    id: Optional[StrictStr] = Field(None, description="Unique identifier for the file")
    bucket: Optional[StrictStr] = Field(None, description="Name of the bucket")
    bucket_id: Optional[StrictInt] = Field(None, alias="bucketId", description="Unique identifier for the bucket")
    filename: Optional[StrictStr] = Field(None, description="Name of the file")
    full_path: Optional[StrictStr] = Field(None, alias="fullPath", description="Full path to the file")
    url: Optional[StrictStr] = Field(None, description="URL to access the file")
    size: Optional[StrictInt] = Field(None, description="Size of the file in bytes")
    type: Optional[StrictStr] = Field(None, description="Type of cloud storage")
    last_modified: Optional[StrictInt] = Field(None, alias="lastModified", description="Timestamp when file was last modified")
    container: Optional[StrictStr] = Field(None, description="Storage container name")
    __properties = ["id", "bucket", "bucketId", "filename", "fullPath", "url", "size", "type", "lastModified", "container"]

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
    def from_json(cls, json_str: str) -> File:
        """Create an instance of File from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> File:
        """Create an instance of File from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return File.parse_obj(obj)

        _obj = File.parse_obj({
            "id": obj.get("id"),
            "bucket": obj.get("bucket"),
            "bucket_id": obj.get("bucketId"),
            "filename": obj.get("filename"),
            "full_path": obj.get("fullPath"),
            "url": obj.get("url"),
            "size": obj.get("size"),
            "type": obj.get("type"),
            "last_modified": obj.get("lastModified"),
            "container": obj.get("container")
        })
        return _obj


