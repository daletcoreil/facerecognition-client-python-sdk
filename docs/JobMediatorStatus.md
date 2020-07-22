# JobMediatorStatus

Current status of the job as reported by the associated Job Processor if the job is committed.  Returned by the GET /jobs/{jobId} call. <br/>jobOutput is a copy of the output specification that was provided when the job was submitted.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Current status of the job as reported by the Job Processor that is handling it, or FAILED if it was rejected (e.g., for missing quota). &lt;br/&gt;Possible transitions - NEW -&gt; QUEUED -&gt; RUNNING -&gt; COMPLETED. | 
**status_message** | **str** | Last message reported by Job Processor handling this job. | [optional] 
**progress** | **int** | Progress as reported by the Job Processor. (TBD) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


