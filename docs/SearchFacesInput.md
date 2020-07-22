# SearchFacesInput

Search an input face image within a cluster.  Returns an array of clusters that are similar to the face.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_image** | [**Locator**](Locator.md) |  | 
**cluster_collection_id** | **str** | ID of a ClusterCollection produced by an ClusterFaces job | [optional] 
**similarity_threshold** | **float** | Similarity threshold (from 0 to 1) over which face candidates are considered a result. | [optional] [default to 0.8]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


