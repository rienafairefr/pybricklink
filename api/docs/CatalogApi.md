# bricklink.CatalogApi

All URIs are relative to *https://api.bricklink.com/api/store/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**items_type_no_get**](CatalogApi.md#items_type_no_get) | **GET** /items/{type}/no | 


# **items_type_no_get**
> object items_type_no_get(type, _false)



### Example

```python
from __future__ import print_function
import time
import bricklink
from bricklink.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = bricklink.CatalogApi()
type = 'type_example' # str | The type of the item to get.
_false = '_false_example' # str | Identification number of the item

try:
    api_response = api_instance.items_type_no_get(type, _false)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogApi->items_type_no_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type of the item to get. | 
 **_false** | **str**| Identification number of the item | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | item data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

