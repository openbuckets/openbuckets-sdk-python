# BucketSearchResultsQuery

The query parameters used for the search.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | The sort direction. | [optional] 
**exact** | **bool** | Whether the search is an exact match. | [optional] 
**keywords** | **str** | The keywords used for the search. | [optional] 
**limit** | **int** | The maximum number of results to return. | [optional] 
**order** | **str** | The field by which to order the results. | [optional] 
**start** | **int** | The starting index for the results. | [optional] 
**type** | **str** | The type of cloud provider. | [optional] 

## Example

```python
from openbuckets.models.bucket_search_results_query import BucketSearchResultsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of BucketSearchResultsQuery from a JSON string
bucket_search_results_query_instance = BucketSearchResultsQuery.from_json(json)
# print the JSON string representation of the object
print BucketSearchResultsQuery.to_json()

# convert the object into a dict
bucket_search_results_query_dict = bucket_search_results_query_instance.to_dict()
# create an instance of BucketSearchResultsQuery from a dict
bucket_search_results_query_form_dict = bucket_search_results_query.from_dict(bucket_search_results_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


