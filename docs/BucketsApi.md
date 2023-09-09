# openbuckets.BucketsApi

All URIs are relative to *https://api.openbuckets.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_buckets**](BucketsApi.md#search_buckets) | **GET** /api/v2/buckets | Search Buckets


# **search_buckets**
> BucketSearchResults search_buckets(keywords=keywords, type=type, exact=exact, start=start, limit=limit, order=order, direction=direction)

Search Buckets

This request enables you to perform a targeted search for buckets within the OpenBuckets database using advanced filters. You can narrow down the search based on various criteria such as keywords, bucket type, exact match, sorting, and pagination.

### Example

* Bearer (auth-scheme) Authentication (bearerAuth):
```python
import time
import os
import openbuckets
from openbuckets.models.bucket_search_results import BucketSearchResults
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
    api_instance = openbuckets.BucketsApi(api_client)
    keywords = 'abg' # str | the search keywords to filter bucket names (e.g., \"abg\") (optional)
    type = 'aws' # str | the type of bucket to filter (e.g., aws,dos,azure,gcp) (optional)
    exact = 0 # float | whether to perform an exact match for the keywords (0 for false, 1 for true) (optional)
    start = 0 # float | starting index for pagination (optional)
    limit = 1000 # float | number of search results to return per page (optional)
    order = 'fileCount' # str | the sorting field for the search results (e.g., \"fileCount\" for sorting by file count) (optional)
    direction = 'asc' # str | the sorting direction for the search results (e.g., \"asc\" for ascending) (optional)

    try:
        # Search Buckets
        api_response = api_instance.search_buckets(keywords=keywords, type=type, exact=exact, start=start, limit=limit, order=order, direction=direction)
        print("The response of BucketsApi->search_buckets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BucketsApi->search_buckets: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | **str**| the search keywords to filter bucket names (e.g., \&quot;abg\&quot;) | [optional] 
 **type** | **str**| the type of bucket to filter (e.g., aws,dos,azure,gcp) | [optional] 
 **exact** | **float**| whether to perform an exact match for the keywords (0 for false, 1 for true) | [optional] 
 **start** | **float**| starting index for pagination | [optional] 
 **limit** | **float**| number of search results to return per page | [optional] 
 **order** | **str**| the sorting field for the search results (e.g., \&quot;fileCount\&quot; for sorting by file count) | [optional] 
 **direction** | **str**| the sorting direction for the search results (e.g., \&quot;asc\&quot; for ascending) | [optional] 

### Return type

[**BucketSearchResults**](BucketSearchResults.md)

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

