# Copyright 2014,  Doug Wiegley,  A10 Networks.
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

import acos_client.v21.base as base


class Server(base.BaseV21):

    def get(self, name, **kwargs):
        return self._post("slb.server.search", {'name': name}, **kwargs)

    def create(self, name, ip_address, **kwargs):
        params = {
            "server": {
                "name": name,
                "host": ip_address,
            }
        }
        self._post("slb.server.create", params, **kwargs)

    def delete(self, name, **kwargs):
        self._post("slb.server.delete", {"server": {"name": name}}, **kwargs)
