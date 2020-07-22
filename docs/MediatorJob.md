# MediatorJob

After a job is submitted to the Dalet Media Mediator service, it is attributed metadata that helps track its lifecycle.  In addition to the input field (Job input / Job output), the JobMediatorEntity provides a unique ID, date created and last modified and usage information (verified quantity and usage ID to reconcile with invoice).  These additional fields are all computed by the mediator and read-only.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Job ID computed by the Dalet Media Mediator Job registry.  Uniquely identifies the job after it has been accepted by the mediator. | 
**date_created** | **str** | Datetime when the job was accepted by the Mediator | 
**date_modified** | **str** | Datetime when the job was last updated by a Job Processor service reporting progress on this job. | 
**quantity** | **int** | Verified number of units after the job is completed.  Units depend on the job profile (usually, they correspond to the duration of the media).  Invoicing is based on this value, which may be different from the one submitted by the client. | 
**status** | [**JobMediatorStatus**](JobMediatorStatus.md) |  | 
**job_output** | [**JobOutput**](JobOutput.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


