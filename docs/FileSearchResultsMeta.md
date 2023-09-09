# FileSearchResultsMeta

Metadata about the search results.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | **float** | The total number of results. | [optional] 

## Example

```python
from openbuckets.models.file_search_results_meta import FileSearchResultsMeta

# TODO update the JSON string below
json = "{}"
# create an instance of FileSearchResultsMeta from a JSON string
file_search_results_meta_instance = FileSearchResultsMeta.from_json(json)
# print the JSON string representation of the object
print FileSearchResultsMeta.to_json()

# convert the object into a dict
file_search_results_meta_dict = file_search_results_meta_instance.to_dict()
# create an instance of FileSearchResultsMeta from a dict
file_search_results_meta_form_dict = file_search_results_meta.from_dict(file_search_results_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


