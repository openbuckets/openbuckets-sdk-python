# FileSearchResultsQuery

The query parameters used for the search.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keywords** | **str** | The keywords used for the search. | [optional] 
**limit** | **float** | The maximum number of results to return. | [optional] 
**start** | **float** | The starting index for the results. | [optional] 

## Example

```python
from openbuckets.models.file_search_results_query import FileSearchResultsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of FileSearchResultsQuery from a JSON string
file_search_results_query_instance = FileSearchResultsQuery.from_json(json)
# print the JSON string representation of the object
print FileSearchResultsQuery.to_json()

# convert the object into a dict
file_search_results_query_dict = file_search_results_query_instance.to_dict()
# create an instance of FileSearchResultsQuery from a dict
file_search_results_query_form_dict = file_search_results_query.from_dict(file_search_results_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


