# ClusterFacesInputAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**face_extraction_id** | **str** | ID of a FaceCollection produced by an ExtractFaces job | 
**cluster_collection_id** | **str** | Optional field - if provided, cluster faces of the input collectionId into an existing clusterCollection, else create a new clusterCollection. | [optional] [default to '']
**minimum_cluster_size** | **float** | Minimum number of images in a cluster.  Clusters with less candidates than this number will be filtered out. | [optional] [default to 2]
**similarity_threshold** | **float** | Similarity threshold (from 0 to 1) over which face candidates are grouped into a cluster.  Higher value produces more smaller clusters with higher confidence. | [optional] [default to 0.5]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


