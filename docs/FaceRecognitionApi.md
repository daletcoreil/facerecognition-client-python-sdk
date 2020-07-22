# facerecognition_client.FaceRecognitionApi

All URIs are relative to *https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_collection**](FaceRecognitionApi.md#get_cluster_collection) | **GET** /face-recognition/cluster-collection/{uid} | 
[**get_face**](FaceRecognitionApi.md#get_face) | **GET** /face-recognition/face/{uid} | 
[**get_face_extraction_collection**](FaceRecognitionApi.md#get_face_extraction_collection) | **GET** /face-recognition/face-extraction-collection/{uid} | 


# **get_cluster_collection**
> ClusterCollection get_cluster_collection(project_service_id, uid)



Retrieve metadata about clusters stored in a clusterCollection created by a ClusterFaces jobs

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
    api_instance = facerecognition_client.FaceRecognitionApi(api_client)
    project_service_id = 'project_service_id_example' # str | Project service id of the client associated to the request
uid = 'uid_example' # str | Cluster Collection Id

    try:
        api_response = api_instance.get_cluster_collection(project_service_id, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FaceRecognitionApi->get_cluster_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_service_id** | **str**| Project service id of the client associated to the request | 
 **uid** | **str**| Cluster Collection Id | 

### Return type

[**ClusterCollection**](ClusterCollection.md)

### Authorization

[tokenSignature](../README.md#tokenSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Bad request |  -  |
**401** | Authorization request fail |  -  |
**502** | Failed request.  Reason is most likely quota violation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_face**
> Face get_face(project_service_id, uid)



Retrieve information for given extracted face id.

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
    api_instance = facerecognition_client.FaceRecognitionApi(api_client)
    project_service_id = 'project_service_id_example' # str | Project service id of the client associated to the request
uid = 'uid_example' # str | Face Id

    try:
        api_response = api_instance.get_face(project_service_id, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FaceRecognitionApi->get_face: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_service_id** | **str**| Project service id of the client associated to the request | 
 **uid** | **str**| Face Id | 

### Return type

[**Face**](Face.md)

### Authorization

[tokenSignature](../README.md#tokenSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Bad request |  -  |
**401** | Authorization request fail |  -  |
**502** | Failed request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_face_extraction_collection**
> FaceExtractionCollection get_face_extraction_collection(project_service_id, uid)



Retrieve the list of FaceIds found in a collection of faces obtained by one extraction job.

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
    api_instance = facerecognition_client.FaceRecognitionApi(api_client)
    project_service_id = 'project_service_id_example' # str | Project service id of the client associated to the request
uid = 'uid_example' # str | Face Collection Extraction Id

    try:
        api_response = api_instance.get_face_extraction_collection(project_service_id, uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling FaceRecognitionApi->get_face_extraction_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_service_id** | **str**| Project service id of the client associated to the request | 
 **uid** | **str**| Face Collection Extraction Id | 

### Return type

[**FaceExtractionCollection**](FaceExtractionCollection.md)

### Authorization

[tokenSignature](../README.md#tokenSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |
**400** | Bad request |  -  |
**401** | Authorization request fail |  -  |
**502** | Failed request.  Reason is most likely quota violation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

