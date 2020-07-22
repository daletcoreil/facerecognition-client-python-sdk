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


class ClusterFacesOutput(object):
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
        'cluster_collection_id': 'str',
        'n_clusters': 'float'
    }

    attribute_map = {
        'cluster_collection_id': 'clusterCollectionId',
        'n_clusters': 'nClusters'
    }

    def __init__(self, cluster_collection_id=None, n_clusters=None, local_vars_configuration=None):  # noqa: E501
        """ClusterFacesOutput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._cluster_collection_id = None
        self._n_clusters = None
        self.discriminator = None

        if cluster_collection_id is not None:
            self.cluster_collection_id = cluster_collection_id
        if n_clusters is not None:
            self.n_clusters = n_clusters

    @property
    def cluster_collection_id(self):
        """Gets the cluster_collection_id of this ClusterFacesOutput.  # noqa: E501

        UID referring to the clusterCollectionId generated or updated by the job.  # noqa: E501

        :return: The cluster_collection_id of this ClusterFacesOutput.  # noqa: E501
        :rtype: str
        """
        return self._cluster_collection_id

    @cluster_collection_id.setter
    def cluster_collection_id(self, cluster_collection_id):
        """Sets the cluster_collection_id of this ClusterFacesOutput.

        UID referring to the clusterCollectionId generated or updated by the job.  # noqa: E501

        :param cluster_collection_id: The cluster_collection_id of this ClusterFacesOutput.  # noqa: E501
        :type: str
        """

        self._cluster_collection_id = cluster_collection_id

    @property
    def n_clusters(self):
        """Gets the n_clusters of this ClusterFacesOutput.  # noqa: E501

        Number of clusters in the created or updated clusterCollection.  # noqa: E501

        :return: The n_clusters of this ClusterFacesOutput.  # noqa: E501
        :rtype: float
        """
        return self._n_clusters

    @n_clusters.setter
    def n_clusters(self, n_clusters):
        """Sets the n_clusters of this ClusterFacesOutput.

        Number of clusters in the created or updated clusterCollection.  # noqa: E501

        :param n_clusters: The n_clusters of this ClusterFacesOutput.  # noqa: E501
        :type: float
        """

        self._n_clusters = n_clusters

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
        if not isinstance(other, ClusterFacesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterFacesOutput):
            return True

        return self.to_dict() != other.to_dict()
