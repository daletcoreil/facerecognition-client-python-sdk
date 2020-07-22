# ExtractFacesInputAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effort** | **str** | How much effort should be invested in extracting faces from the video stream. More effort brings higher accuracy for higher cost. | [optional] [default to 'Normal']
**minimum_facesize** | **float** | Minimum size of face in pixel.  Only extract a face if its bounding box is larger than this size. | [optional] [default to 40]
**face_size** | **float** | Extraction Image size in pixels.  Extracted faces are normalized as squared bitmaps with  this size.  Colors are also normalized. | [optional] [default to 160]
**video** | [**Locator**](Locator.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


