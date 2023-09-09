# File


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the file | [optional] 
**bucket** | **str** | Name of the bucket | [optional] 
**bucket_id** | **int** | Unique identifier for the bucket | [optional] 
**filename** | **str** | Name of the file | [optional] 
**full_path** | **str** | Full path to the file | [optional] 
**url** | **str** | URL to access the file | [optional] 
**size** | **int** | Size of the file in bytes | [optional] 
**type** | **str** | Type of cloud storage | [optional] 
**last_modified** | **int** | Timestamp when file was last modified | [optional] 
**container** | **str** | Storage container name | [optional] 

## Example

```python
from openbuckets.models.file import File

# TODO update the JSON string below
json = "{}"
# create an instance of File from a JSON string
file_instance = File.from_json(json)
# print the JSON string representation of the object
print File.to_json()

# convert the object into a dict
file_dict = file_instance.to_dict()
# create an instance of File from a dict
file_form_dict = file.from_dict(file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


