# facerecognition_client.AuthApi

All URIs are relative to *https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token**](AuthApi.md#get_access_token) | **POST** /auth/access-token | 


# **get_access_token**
> Token get_access_token(client, secret)



Generate new access token

### Example

```python
from __future__ import print_function
import time
import facerecognition_client
from facerecognition_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod
# See configuration.py for a list of all supported configuration parameters.
configuration = facerecognition_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod"
)


# Enter a context with an instance of the API client
with facerecognition_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = facerecognition_client.AuthApi(api_client)
    client = 'client_example' # str | client_id of the application
secret = 'secret_example' # str | secret_key of the application

    try:
        api_response = api_instance.get_access_token(client, secret)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AuthApi->get_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | **str**| client_id of the application | 
 **secret** | **str**| secret_key of the application | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**401** | Invalid secret or client |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

