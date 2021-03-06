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


class ClusterCollection(object):
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
        'uid': 'str',
        'tenant_id': 'str',
        'project_service_id': 'str',
        'job_id': 'str',
        'created_at': 'datetime',
        'created_by': 'str',
        'modified_at': 'datetime',
        'modified_by': 'str',
        'name': 'str',
        'clusters': 'list[Cluster]'
    }

    attribute_map = {
        'uid': 'uid',
        'tenant_id': 'tenantId',
        'project_service_id': 'projectServiceId',
        'job_id': 'jobId',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'modified_at': 'modifiedAt',
        'modified_by': 'modifiedBy',
        'name': 'name',
        'clusters': 'clusters'
    }

    def __init__(self, uid=None, tenant_id=None, project_service_id=None, job_id=None, created_at=None, created_by=None, modified_at=None, modified_by=None, name=None, clusters=None, local_vars_configuration=None):  # noqa: E501
        """ClusterCollection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._uid = None
        self._tenant_id = None
        self._project_service_id = None
        self._job_id = None
        self._created_at = None
        self._created_by = None
        self._modified_at = None
        self._modified_by = None
        self._name = None
        self._clusters = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if project_service_id is not None:
            self.project_service_id = project_service_id
        if job_id is not None:
            self.job_id = job_id
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if modified_at is not None:
            self.modified_at = modified_at
        if modified_by is not None:
            self.modified_by = modified_by
        if name is not None:
            self.name = name
        self.clusters = clusters

    @property
    def uid(self):
        """Gets the uid of this ClusterCollection.  # noqa: E501


        :return: The uid of this ClusterCollection.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ClusterCollection.


        :param uid: The uid of this ClusterCollection.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def tenant_id(self):
        """Gets the tenant_id of this ClusterCollection.  # noqa: E501


        :return: The tenant_id of this ClusterCollection.  # noqa: E501
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this ClusterCollection.


        :param tenant_id: The tenant_id of this ClusterCollection.  # noqa: E501
        :type: str
        """

        self._tenant_id = tenant_id

    @property
    def project_service_id(self):
        """Gets the project_service_id of this ClusterCollection.  # noqa: E501


        :return: The project_service_id of this ClusterCollection.  # noqa: E501
        :rtype: str
        """
        return self._project_service_id

    @project_service_id.setter
    def project_service_id(self, project_service_id):
        """Sets the project_service_id of this ClusterCollection.


        :param project_service_id: The project_service_id of this ClusterCollection.  # noqa: E501
        :type: str
        """

        self._project_service_id = project_service_id

    @property
    def job_id(self):
        """Gets the job_id of this ClusterCollection.  # noqa: E501

        Cluster collections are initially created by a Cluster job - they can be then curated manually  # noqa: E501

        :return: The job_id of this ClusterCollection.  # noqa: E501
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        """Sets the job_id of this ClusterCollection.

        Cluster collections are initially created by a Cluster job - they can be then curated manually  # noqa: E501

        :param job_id: The job_id of this ClusterCollection.  # noqa: E501
        :type: str
        """

        self._job_id = job_id

    @property
    def created_at(self):
        """Gets the created_at of this ClusterCollection.  # noqa: E501


        :return: The created_at of this ClusterCollection.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ClusterCollection.


        :param created_at: The created_at of this ClusterCollection.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this ClusterCollection.  # noqa: E501

        if created by a job - jobId else name of person who created the clusterCollection  # noqa: E501

        :return: The created_by of this ClusterCollection.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ClusterCollection.

        if created by a job - jobId else name of person who created the clusterCollection  # noqa: E501

        :param created_by: The created_by of this ClusterCollection.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modified_at(self):
        """Gets the modified_at of this ClusterCollection.  # noqa: E501


        :return: The modified_at of this ClusterCollection.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this ClusterCollection.


        :param modified_at: The modified_at of this ClusterCollection.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def modified_by(self):
        """Gets the modified_by of this ClusterCollection.  # noqa: E501


        :return: The modified_by of this ClusterCollection.  # noqa: E501
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this ClusterCollection.


        :param modified_by: The modified_by of this ClusterCollection.  # noqa: E501
        :type: str
        """

        self._modified_by = modified_by

    @property
    def name(self):
        """Gets the name of this ClusterCollection.  # noqa: E501

        descriptive name of the cluster collection  # noqa: E501

        :return: The name of this ClusterCollection.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterCollection.

        descriptive name of the cluster collection  # noqa: E501

        :param name: The name of this ClusterCollection.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def clusters(self):
        """Gets the clusters of this ClusterCollection.  # noqa: E501

        metadata about cluster found in the ClusterCollection  # noqa: E501

        :return: The clusters of this ClusterCollection.  # noqa: E501
        :rtype: list[Cluster]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """Sets the clusters of this ClusterCollection.

        metadata about cluster found in the ClusterCollection  # noqa: E501

        :param clusters: The clusters of this ClusterCollection.  # noqa: E501
        :type: list[Cluster]
        """
        if self.local_vars_configuration.client_side_validation and clusters is None:  # noqa: E501
            raise ValueError("Invalid value for `clusters`, must not be `None`")  # noqa: E501

        self._clusters = clusters

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
        if not isinstance(other, ClusterCollection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ClusterCollection):
            return True

        return self.to_dict() != other.to_dict()
