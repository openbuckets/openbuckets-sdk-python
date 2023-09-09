# BucketSearchResults


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Total number of matching buckets | [optional] 
**results** | [**List[Bucket]**](Bucket.md) |  | [optional] 

## Example

```python
from openbuckets.models.bucket_search_results import BucketSearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of BucketSearchResults from a JSON string
bucket_search_results_instance = BucketSearchResults.from_json(json)
# print the JSON string representation of the object
print BucketSearchResults.to_json()

# convert the object into a dict
bucket_search_results_dict = bucket_search_results_instance.to_dict()
# create an instance of BucketSearchResults from a dict
bucket_search_results_form_dict = bucket_search_results.from_dict(bucket_search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


