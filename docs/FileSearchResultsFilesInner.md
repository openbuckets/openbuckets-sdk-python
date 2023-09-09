# FileSearchResultsFilesInner

Details about each file.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_id** | **float** | The unique identifier for the bucket containing the file. | [optional] 
**cloud_provider** | **str** | The cloud provider where the file is hosted. | [optional] 
**file_extension** | **str** | The file extension. | [optional] 
**file_name** | **str** | The name of the file. | [optional] 
**file_size** | **float** | The size of the file in bytes. | [optional] 
**file_url** | **str** | The URL of the file. | [optional] 
**full_path** | **str** | The full path to the file. | [optional] 
**id** | **float** | The unique identifier for the file. | [optional] 
**indexed_at** | **datetime** | The date and time when the file was last indexed. | [optional] 
**last_modified** | **datetime** | The date and time when the file was last modified. | [optional] 

## Example

```python
from openbuckets.models.file_search_results_files_inner import FileSearchResultsFilesInner

# TODO update the JSON string below
json = "{}"
# create an instance of FileSearchResultsFilesInner from a JSON string
file_search_results_files_inner_instance = FileSearchResultsFilesInner.from_json(json)
# print the JSON string representation of the object
print FileSearchResultsFilesInner.to_json()

# convert the object into a dict
file_search_results_files_inner_dict = file_search_results_files_inner_instance.to_dict()
# create an instance of FileSearchResultsFilesInner from a dict
file_search_results_files_inner_form_dict = file_search_results_files_inner.from_dict(file_search_results_files_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


