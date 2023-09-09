# openbuckets.FilesApi

All URIs are relative to *https://api.openbuckets.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_files**](FilesApi.md#search_files) | **GET** /api/v2/files | Search Files


# **search_files**
> FileSearchResults search_files(keywords=keywords, order=order, direction=direction, field_to_search=field_to_search, full_path=full_path, extensions=extensions, last_modified_from=last_modified_from, last_modified_to=last_modified_to, size_from=size_from, size_to=size_to, start=start, limit=limit, exclude_buckets=exclude_buckets, buckets=buckets, stop_extensions=stop_extensions)

Search Files

This request allows you to perform a highly specific search for files within the OpenBuckets database using advanced filters. You can narrow down the search based on various criteria such as keywords, order, size, date range, file extensions, and more.

### Example

* Bearer (auth-scheme) Authentication (bearerAuth):
```python
import time
import os
import openbuckets
from openbuckets.models.file_search_results import FileSearchResults
from openbuckets.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.openbuckets.io
# See configuration.py for a list of all supported configuration parameters.
configuration = openbuckets.Configuration(
    host = "https://api.openbuckets.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (auth-scheme): bearerAuth
configuration = openbuckets.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openbuckets.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openbuckets.FilesApi(api_client)
    keywords = 'org images -aws' # str | multiple keywords.\"-\" denotes stop keywords (optional)
    order = 'size' # str | the sorting field for the search results (e.g., \"size\", \"lastModified\") (optional)
    direction = 'desc' # str | the sorting direction for the search results (e.g., \"desc\" for descending) (optional)
    field_to_search = 'desc' # str | taken into consideration if you provide any of the allowed values, \"cloudProvider\",\"fileExtension\",\"fileName\",\"fileUrl\",\"fullPath\" (optional)
    full_path = 1 # float | include the full path in the search results (1 for true, 0 for false) (optional)
    extensions = 'pdf,.env' # str | comma-separated list of file extensions to include (e.g., \"pdf,env\") (optional)
    last_modified_from = '1682965800' # str | UNIX timestamp for the starting date of the last modification range (optional)
    last_modified_to = '1693420200' # str | UNIX timestamp for the ending date of the last modification rang (optional)
    size_from = '15155035' # str | minimum file size in bytes (optional)
    size_to = '4538824351471' # str | maximum file size in bytes (optional)
    start = 0 # float | starting index for pagination (optional)
    limit = 20 # float | number of search results to return per page, based on your role.  If you send a value more than the allowed limit, we set it to the allowed limit. (optional)
    exclude_buckets = '45,54' # str | comma-separated list of bucket IDs to exclude from the search (optional)
    buckets = '' # str | filter search results to specific bucket IDs (optional)
    stop_extensions = '.csv,.env' # str | comma-separated list of file extensions to exclude with or without \".\" (e.g., sql, .sql) (optional)

    try:
        # Search Files
        api_response = api_instance.search_files(keywords=keywords, order=order, direction=direction, field_to_search=field_to_search, full_path=full_path, extensions=extensions, last_modified_from=last_modified_from, last_modified_to=last_modified_to, size_from=size_from, size_to=size_to, start=start, limit=limit, exclude_buckets=exclude_buckets, buckets=buckets, stop_extensions=stop_extensions)
        print("The response of FilesApi->search_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesApi->search_files: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | **str**| multiple keywords.\&quot;-\&quot; denotes stop keywords | [optional] 
 **order** | **str**| the sorting field for the search results (e.g., \&quot;size\&quot;, \&quot;lastModified\&quot;) | [optional] 
 **direction** | **str**| the sorting direction for the search results (e.g., \&quot;desc\&quot; for descending) | [optional] 
 **field_to_search** | **str**| taken into consideration if you provide any of the allowed values, \&quot;cloudProvider\&quot;,\&quot;fileExtension\&quot;,\&quot;fileName\&quot;,\&quot;fileUrl\&quot;,\&quot;fullPath\&quot; | [optional] 
 **full_path** | **float**| include the full path in the search results (1 for true, 0 for false) | [optional] 
 **extensions** | **str**| comma-separated list of file extensions to include (e.g., \&quot;pdf,env\&quot;) | [optional] 
 **last_modified_from** | **str**| UNIX timestamp for the starting date of the last modification range | [optional] 
 **last_modified_to** | **str**| UNIX timestamp for the ending date of the last modification rang | [optional] 
 **size_from** | **str**| minimum file size in bytes | [optional] 
 **size_to** | **str**| maximum file size in bytes | [optional] 
 **start** | **float**| starting index for pagination | [optional] 
 **limit** | **float**| number of search results to return per page, based on your role.  If you send a value more than the allowed limit, we set it to the allowed limit. | [optional] 
 **exclude_buckets** | **str**| comma-separated list of bucket IDs to exclude from the search | [optional] 
 **buckets** | **str**| filter search results to specific bucket IDs | [optional] 
 **stop_extensions** | **str**| comma-separated list of file extensions to exclude with or without \&quot;.\&quot; (e.g., sql, .sql) | [optional] 

### Return type

[**FileSearchResults**](FileSearchResults.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

