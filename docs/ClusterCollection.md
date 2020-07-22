# ClusterCollection

Collection of clusters within which searches can be executed
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uid** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**project_service_id** | **str** |  | [optional] 
**job_id** | **str** | Cluster collections are initially created by a Cluster job - they can be then curated manually | [optional] 
**created_at** | **datetime** |  | [optional] 
**created_by** | **str** | if created by a job - jobId else name of person who created the clusterCollection | [optional] 
**modified_at** | **datetime** |  | [optional] 
**modified_by** | **str** |  | [optional] 
**name** | **str** | descriptive name of the cluster collection | [optional] 
**clusters** | [**list[Cluster]**](Cluster.md) | metadata about cluster found in the ClusterCollection | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


