# facerecognition_client.JobsApi

All URIs are relative to *https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_job**](JobsApi.md#create_job) | **POST** /jobs | 
[**get_job_by_id**](JobsApi.md#get_job_by_id) | **GET** /jobs/{jobId} | 


# **create_job**
> MediatorJob create_job(job_mediator_input)



Submit a new job to the Dalet Media Mediator

### Example

* Api Key Authentication (tokenSignature):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenSignature
configuration = facerecognition_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with facerecognition_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = facerecognition_client.JobsApi(api_client)
    job_mediator_input = {"$ref":"#/components/examples/MediatorJobPost/value"} # JobMediatorInput | Object describing the Job to be executed.

    try:
        api_response = api_instance.create_job(job_mediator_input)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->create_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_mediator_input** | [**JobMediatorInput**](JobMediatorInput.md)| Object describing the Job to be executed. | 

### Return type

[**MediatorJob**](MediatorJob.md)

### Authorization

[tokenSignature](../README.md#tokenSignature)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success response |  -  |
**400** | Bad request |  -  |
**401** | Authorization request fail |  -  |
**502** | Failed request.  Reason is most likely quota violation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_by_id**
> MediatorJob get_job_by_id(job_id)



Get job

### Example

* Api Key Authentication (tokenSignature):
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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenSignature
configuration = facerecognition_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod",
    api_key = {
        'Authorization': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with facerecognition_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = facerecognition_client.JobsApi(api_client)
    job_id = '5b166783-7ab5-39b8-fcb5-6255dd115412' # str | ID of the job as returned in JobMediatorEntity

    try:
        api_response = api_instance.get_job_by_id(job_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobsApi->get_job_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| ID of the job as returned in JobMediatorEntity | 

### Return type

[**MediatorJob**](MediatorJob.md)

### Authorization

[tokenSignature](../README.md#tokenSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**404** | Job with required ID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

