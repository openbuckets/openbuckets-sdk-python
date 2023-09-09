# FileSearchResults

The search results for files.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | [**List[FileSearchResultsFilesInner]**](FileSearchResultsFilesInner.md) | An array of files. | [optional] 
**meta** | [**FileSearchResultsMeta**](FileSearchResultsMeta.md) |  | [optional] 
**query** | [**FileSearchResultsQuery**](FileSearchResultsQuery.md) |  | [optional] 

## Example

```python
from openbuckets.models.file_search_results import FileSearchResults

# TODO update the JSON string below
json = "{}"
# create an instance of FileSearchResults from a JSON string
file_search_results_instance = FileSearchResults.from_json(json)
# print the JSON string representation of the object
print FileSearchResults.to_json()

# convert the object into a dict
file_search_results_dict = file_search_results_instance.to_dict()
# create an instance of FileSearchResults from a dict
file_search_results_form_dict = file_search_results.from_dict(file_search_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


