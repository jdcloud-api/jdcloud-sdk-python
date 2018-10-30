# coding=utf8

# Copyright 2018 JDCLOUD.COM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# NOTE: This class is auto generated by the jdcloud code generator program.

from jdcloud_sdk.core.jdcloudrequest import JDCloudRequest


class CreateAppRequest(JDCloudRequest):
    """
    创建app
    """

    def __init__(self, parameters, header=None, version="v1"):
        super(CreateAppRequest, self).__init__(
            '/regions/{regionId}/app', 'POST', header, version)
        self.parameters = parameters


class CreateAppParameters(object):

    def __init__(self, regionId, ):
        """
        :param regionId: 
        """

        self.regionId = regionId
        self.clientName = None
        self.tokenEndpointAuthMethod = None
        self.grantTypes = None
        self.redirectUris = None
        self.clientUri = None
        self.logoUri = None
        self.tosUri = None
        self.policyUri = None
        self.scope = None
        self.jwksUri = None
        self.jwks = None
        self.contacts = None
        self.extension = None
        self.accessTokenValiditySeconds = None
        self.refreshTokenValiditySeconds = None
        self.multiTenant = None
        self.secret = None
        self.userType = None

    def setClientName(self, clientName):
        """
        :param clientName: (Optional) 应用名
        """
        self.clientName = clientName

    def setTokenEndpointAuthMethod(self, tokenEndpointAuthMethod):
        """
        :param tokenEndpointAuthMethod: (Optional) tokenEndpointAuthMethod
        """
        self.tokenEndpointAuthMethod = tokenEndpointAuthMethod

    def setGrantTypes(self, grantTypes):
        """
        :param grantTypes: (Optional) grantTypes
        """
        self.grantTypes = grantTypes

    def setRedirectUris(self, redirectUris):
        """
        :param redirectUris: (Optional) redirectUris
        """
        self.redirectUris = redirectUris

    def setClientUri(self, clientUri):
        """
        :param clientUri: (Optional) clientUri
        """
        self.clientUri = clientUri

    def setLogoUri(self, logoUri):
        """
        :param logoUri: (Optional) logoUri
        """
        self.logoUri = logoUri

    def setTosUri(self, tosUri):
        """
        :param tosUri: (Optional) tosUri
        """
        self.tosUri = tosUri

    def setPolicyUri(self, policyUri):
        """
        :param policyUri: (Optional) policyUri
        """
        self.policyUri = policyUri

    def setScope(self, scope):
        """
        :param scope: (Optional) scope
        """
        self.scope = scope

    def setJwksUri(self, jwksUri):
        """
        :param jwksUri: (Optional) jwksUri
        """
        self.jwksUri = jwksUri

    def setJwks(self, jwks):
        """
        :param jwks: (Optional) jwks
        """
        self.jwks = jwks

    def setContacts(self, contacts):
        """
        :param contacts: (Optional) contacts
        """
        self.contacts = contacts

    def setExtension(self, extension):
        """
        :param extension: (Optional) extension
        """
        self.extension = extension

    def setAccessTokenValiditySeconds(self, accessTokenValiditySeconds):
        """
        :param accessTokenValiditySeconds: (Optional) accessTokenValiditySeconds
        """
        self.accessTokenValiditySeconds = accessTokenValiditySeconds

    def setRefreshTokenValiditySeconds(self, refreshTokenValiditySeconds):
        """
        :param refreshTokenValiditySeconds: (Optional) refreshTokenValiditySeconds
        """
        self.refreshTokenValiditySeconds = refreshTokenValiditySeconds

    def setMultiTenant(self, multiTenant):
        """
        :param multiTenant: (Optional) multiTenant
        """
        self.multiTenant = multiTenant

    def setSecret(self, secret):
        """
        :param secret: (Optional) secret
        """
        self.secret = secret

    def setUserType(self, userType):
        """
        :param userType: (Optional) userType
        """
        self.userType = userType

