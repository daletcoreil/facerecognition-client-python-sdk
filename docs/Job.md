# Job

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_type** | **str** |  | [optional] 
**job_profile** | **str** | Define what type of job is to be executed on the media object. | [optional] 
**region_name** | **str** | If defined, require job to be run on a Worker instance that can serve any of the regions, else can run on any Worker instance. If no service is available for the requested regions, the job fails. | [optional] 
**max_region_latency** | **float** | If defined, require job to be run on a Worker instance that can access the requested region with a latency less than this value | [optional] [default to 100]
**job_input** | [**JobInput**](JobInput.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


