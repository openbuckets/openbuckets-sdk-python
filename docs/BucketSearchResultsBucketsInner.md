# BucketSearchResultsBucketsInner

Details about each bucket.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_provider** | **str** | The cloud provider where the bucket is hosted. | [optional] 
**file_count** | **int** | The number of files in the bucket. | [optional] 
**id** | **int** | The unique identifier for the bucket. | [optional] 
**indexed_at** | **datetime** | The date and time when the bucket was last indexed. | [optional] 
**url** | **str** | The URL of the bucket. | [optional] 

## Example

```python
from openbuckets.models.bucket_search_results_buckets_inner import BucketSearchResultsBucketsInner

# TODO update the JSON string below
json = "{}"
# create an instance of BucketSearchResultsBucketsInner from a JSON string
bucket_search_results_buckets_inner_instance = BucketSearchResultsBucketsInner.from_json(json)
# print the JSON string representation of the object
print BucketSearchResultsBucketsInner.to_json()

# convert the object into a dict
bucket_search_results_buckets_inner_dict = bucket_search_results_buckets_inner_instance.to_dict()
# create an instance of BucketSearchResultsBucketsInner from a dict
bucket_search_results_buckets_inner_form_dict = bucket_search_results_buckets_inner.from_dict(bucket_search_results_buckets_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


