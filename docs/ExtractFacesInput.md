# ExtractFacesInput

Analyze input video file to detect faces. Steps of analysis include frame extraction, selection of frames, detection of faces, encoding of the faces using a neural network encoder backbone, normalization of the extracted faces and storage of the result in a persistent FaceCollection.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effort** | **str** | How much effort should be invested in extracting faces from the video stream. More effort brings higher accuracy for higher cost. | [optional] [default to 'Normal']
**minimum_facesize** | **float** | Minimum size of face in pixel.  Only extract a face if its bounding box is larger than this size. | [optional] [default to 40]
**face_size** | **float** | Extraction Image size in pixels.  Extracted faces are normalized as squared bitmaps with  this size.  Colors are also normalized. | [optional] [default to 160]
**video** | [**Locator**](Locator.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


