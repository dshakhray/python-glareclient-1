# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


from glareclient.common import http
from glareclient.common import utils
from glareclient.v1 import artifacts
from glareclient.v1 import versions


class Client(object):
    """Client for the Glare Artifact Repository v2 API.

    :param string endpoint: A user-supplied endpoint URL for the glare
                            service.
    :param string token: Token for authentication.
    :param integer timeout: Allows customization of the timeout for client
                            http requests. (optional)
    :param string language_header: Set Accept-Language header to be sent in
                                   requests to glare.
    """

    def __init__(self, endpoint=None, **kwargs):
        endpoint, self.version = utils.endpoint_version_from_url(endpoint, 1.0)
        self.http_client = http.get_http_client(endpoint=endpoint, **kwargs)

        self.artifacts = artifacts.Controller(self.http_client)
        self.versions = versions.VersionController(self.http_client)
