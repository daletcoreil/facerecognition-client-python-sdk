# JobMediatorInput

Toplevel description of any job submitted to the Dalet Media Mediator service.  Encapsulates a service specific job description with authentication, billing and tracking metadata.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_service_id** | **str** | Customer Project ID.  This ID must be provided by Dalet when a Cortex service is provisioned.  It must match the authorization token you have been provided. | 
**quantity** | **int** | Number of units that will be charged for this job.  The unit depends on the job profile.  For example, for an AI metadata extraction job, units are seconds of media duration. | 
**tracking** | [**object**](.md) | Client metadata associated to the job.  This can include any identification fields provided by the client. It should identify the job in a unique manner and is useful to reconcile usage reports with client metadata. | [optional] 
**notification_endpoint** | **str** | Callback URL endpoint to be called once the stage of the job is changed. | [optional] 
**job** | [**Job**](Job.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


