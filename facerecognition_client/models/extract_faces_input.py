# coding: utf-8

"""
    Dalet Media Mediator API

    # Scope Dalet Mediator API allows you to submit long running media jobs managed by Dalet services.  Long running media jobs include: - **Media processing** such as transcoding or automatic QC. - **Automatic metadata extraction** such as automatic speech transcription or face detection.  The Dalet Mediator API is a REST API with typed schema for the payload. # Architecture Job processing is performed on the cloud via dynamic combination of microservices. Dalet Mediator adopts the [EBU MCMA] architecture.  The key objectives of this architecture are to support: - Job management and monitoring - Long running transactions - Event based communication pattern - Service registration and discovery - Horizontal scalability in an elastic manner  The architecture is implemented using the serverless approach - relying on  independent microservices accessible through well documented REST endpoints and sharing a common object model. ## Roles The following services are involved in the processing of media jobs exposed through the Dalet Media Mediator API: - **Mediator**: this is the main entry point to the architecture; this API endpoint supports: 1. Checking authentication using an API key and a token mechanism 2. Verifying quota restrictions before accepting a submitted job 3. Keeping track of usage so that job processing can be tracked and billed 4. Keeping track of jobs metadata as a job repository - **Job Processor**: once a job request is accepted by the mediator, it is assigned to a Job Processor. The Job Processor dispatches the job to an appropriate Job Worker (depending on the job profile and other criteria such as load on the system and cost of operation).  It then keeps track of the progress of the job and its status until completion and possible failures and timeout.  It reports progress to the Mediator through notifications. - **Job Worker**: The Job Worker performs the actual work on the media object, for example, AI metadata extraction (AME) or essence transcoding.  It reports progress to the Job Processor through notifications. - **Service Registry**: The Service Registry keeps track of all active services in the architecture. It is queried by the Mediator and by Processors to discover candidate services to perform jobs.  It is updated whenever a new service is launched or stopped.  The Service Registry also stores the list of all job profiles supported by one of the Job Workers deployed in the architecture. The Dalet Mediator API abstracts away from the complexity of this orchestration and provides a simple endpoint to submit long running jobs and monitor the progress of their execution.  It serves as a facade for the additional technical services for authentication, usage monitoring and service registry.  [EBU MCMA]: /https://tech.ebu.ch/groups/mcma 'EBU MCMA' ## Job Lifecycle ![Job Lifecyle Diagram](./job_lifecycle.svg 'Job Lifecycle Diagram')  ## Authentication To use the Dalet Mediator API - you must obtain an APIKey from Dalet.  This key comes in the form of two parameters: * client ID * secret  Given these two parameters, a client program must first obtain an access token (GET /auth/access-token) and then associate this token to every subsequent calls.  When the token expires, the API will return a 401 error code.  In this case, the client must request a new token and resubmit the request.   # noqa: E501

    The version of the OpenAPI document: 1.4.0
    Contact: cortexsupport@dalet.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from facerecognition_client.configuration import Configuration


class ExtractFacesInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'effort': 'str',
        'minimum_facesize': 'float',
        'face_size': 'float',
        'video': 'Locator'
    }

    attribute_map = {
        'effort': 'effort',
        'minimum_facesize': 'minimumFacesize',
        'face_size': 'faceSize',
        'video': 'video'
    }

    def __init__(self, effort='Normal', minimum_facesize=40, face_size=160, video=None, local_vars_configuration=None):  # noqa: E501
        """ExtractFacesInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._effort = None
        self._minimum_facesize = None
        self._face_size = None
        self._video = None
        self.discriminator = None

        if effort is not None:
            self.effort = effort
        if minimum_facesize is not None:
            self.minimum_facesize = minimum_facesize
        if face_size is not None:
            self.face_size = face_size
        self.video = video

    @property
    def effort(self):
        """Gets the effort of this ExtractFacesInput.  # noqa: E501

        How much effort should be invested in extracting faces from the video stream. More effort brings higher accuracy for higher cost.  # noqa: E501

        :return: The effort of this ExtractFacesInput.  # noqa: E501
        :rtype: str
        """
        return self._effort

    @effort.setter
    def effort(self, effort):
        """Sets the effort of this ExtractFacesInput.

        How much effort should be invested in extracting faces from the video stream. More effort brings higher accuracy for higher cost.  # noqa: E501

        :param effort: The effort of this ExtractFacesInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["Low", "Basic", "Normal", "High", "Extreme"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and effort not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `effort` ({0}), must be one of {1}"  # noqa: E501
                .format(effort, allowed_values)
            )

        self._effort = effort

    @property
    def minimum_facesize(self):
        """Gets the minimum_facesize of this ExtractFacesInput.  # noqa: E501

        Minimum size of face in pixel.  Only extract a face if its bounding box is larger than this size.  # noqa: E501

        :return: The minimum_facesize of this ExtractFacesInput.  # noqa: E501
        :rtype: float
        """
        return self._minimum_facesize

    @minimum_facesize.setter
    def minimum_facesize(self, minimum_facesize):
        """Sets the minimum_facesize of this ExtractFacesInput.

        Minimum size of face in pixel.  Only extract a face if its bounding box is larger than this size.  # noqa: E501

        :param minimum_facesize: The minimum_facesize of this ExtractFacesInput.  # noqa: E501
        :type: float
        """

        self._minimum_facesize = minimum_facesize

    @property
    def face_size(self):
        """Gets the face_size of this ExtractFacesInput.  # noqa: E501

        Extraction Image size in pixels.  Extracted faces are normalized as squared bitmaps with  this size.  Colors are also normalized.  # noqa: E501

        :return: The face_size of this ExtractFacesInput.  # noqa: E501
        :rtype: float
        """
        return self._face_size

    @face_size.setter
    def face_size(self, face_size):
        """Sets the face_size of this ExtractFacesInput.

        Extraction Image size in pixels.  Extracted faces are normalized as squared bitmaps with  this size.  Colors are also normalized.  # noqa: E501

        :param face_size: The face_size of this ExtractFacesInput.  # noqa: E501
        :type: float
        """

        self._face_size = face_size

    @property
    def video(self):
        """Gets the video of this ExtractFacesInput.  # noqa: E501


        :return: The video of this ExtractFacesInput.  # noqa: E501
        :rtype: Locator
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this ExtractFacesInput.


        :param video: The video of this ExtractFacesInput.  # noqa: E501
        :type: Locator
        """
        if self.local_vars_configuration.client_side_validation and video is None:  # noqa: E501
            raise ValueError("Invalid value for `video`, must not be `None`")  # noqa: E501

        self._video = video

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExtractFacesInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExtractFacesInput):
            return True

        return self.to_dict() != other.to_dict()
