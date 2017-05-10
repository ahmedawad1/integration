#!/usr/bin/python
# Copyright 2016 Mender Software AS
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        https://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.


import requests
from fabric.api import *
from common import *
from common_docker import *
from MenderAPI import api_version


class DeviceAuthentication(object):
    auth = None

    def __init__(self, auth):
        self.auth = auth

    def get_deviceauth_base_path(self):
        return "https://%s/api/management/%s/devauth/devices/" % (get_mender_gateway(), api_version)

    def decommission(self, deviceID, expected_http_code=204):
        decommission_path_url = self.get_deviceauth_base_path() + str(deviceID)
        r = requests.delete(decommission_path_url,
                            verify=False,
                            headers=self.auth.get_auth_token())
        print(decommission_path_url, r.status_code)
        assert r.status_code == expected_http_code
