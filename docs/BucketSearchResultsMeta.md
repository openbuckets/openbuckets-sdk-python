# BucketSearchResultsMeta

Metadata about the search results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **int** | The total number of results. | [optional] 

## Example

```python
from openbuckets.models.bucket_search_results_meta import BucketSearchResultsMeta

# TODO update the JSON string below
json = "{}"
# create an instance of BucketSearchResultsMeta from a JSON string
bucket_search_results_meta_instance = BucketSearchResultsMeta.from_json(json)
# print the JSON string representation of the object
print BucketSearchResultsMeta.to_json()

# convert the object into a dict
bucket_search_results_meta_dict = bucket_search_results_meta_instance.to_dict()
# create an instance of BucketSearchResultsMeta from a dict
bucket_search_results_meta_form_dict = bucket_search_results_meta.from_dict(bucket_search_results_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


