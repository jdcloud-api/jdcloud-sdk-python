# coding=utf8

import unittest
from signer import Signer
from credential import Credential
from logger import Logger
from util import *
from . import const


class SignerTest(unittest.TestCase):

    def setUp(self):
        access_key = 'ak'
        secret_key = 'sk'
        self.credential = Credential(access_key, secret_key)
        self.logger = Logger(3) # FATAL = 0 ERROR = 1 WARN = 2 INFO = 3

        self.service_name = 'apigatewaytestproductline'
        self.region = 'cn-north-1'
        self.method = 'GET'
        self.host = 'http://apigw-internal-dev.cn-north-1.jcloudcs.com:8000'
        self.ori_path = '/v1/regions/cn-north-1/instances'
        self.path = ''
        self.query = ''
        self.header = {'x-jdcloud-date' : '20190917T064708Z', 'x-jdcloud-nonce' : 'X-Jdcloud-Nonce', 'content-type' : 'application/json'}

    def tearDown(self):
        return

    def testSign_path_specialCharacters(self):
        signer = Signer(self.logger)
        ori_path = '/v1/regions/cn-north-1/instances/ /`!@#$%^&*()=+/0123456789/[]\\;\',<>?:"{}|/abcdefghijklmnopqrstuvwxyz/ABCDEFGHIJKLMNOPQRSTUVWXYZ/-_.~:GET'

        signer.signV3(method=self.method, region=self.region, host=self.host, path=ori_path, query=self.query,
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=925b9455228ef23ee7ec2dd3e33f7e645bcbcb3f4732894c17e4a0cf1d41d1e6'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_path_chineseCharacters(self):
        signer = Signer(self.logger)
        ori_path = '/v1/regions/cn-north-1/instances/中文:GET'

        signer.signV3(method=self.method, region=self.region, host=self.host, path=ori_path, query=self.query,
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=936ed2dcb6fb4271ad640e0f46f1fe61763a0bad8bb4f4eb1224261f969612fa'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_path_null(self):
        signer = Signer(self.logger)
        ori_path = ''

        signer.signV3(method=self.method, region=self.region, host=self.host, path=ori_path, query=self.query,
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=44c5ec30b6185516986ae171d8276552bc0f37f6a536a44e4f578958fc1c12be'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_path_nullSlashes(self):
        signer = Signer(self.logger)
        ori_path = 'v1'

        signer.signV3(method=self.method, region=self.region, host=self.host, path=ori_path, query=self.query,
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=92cd3ed582c13af58b4c81ddad150c350e656c6cc9e78ec154d7385e499b91b6'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_path_endSlashes(self):
        signer = Signer(self.logger)
        ori_path = 'v1/'

        signer.signV3(method=self.method, region=self.region, host=self.host, path=ori_path, query=self.query,
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=035689ae2ce6a3603928ac3d60a6d2fbfb550d33c5da983342a6356419ccd914'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_path_doubleSlashes(self):
        signer = Signer(self.logger)
        ori_path = '///v1/regions/cn-north-1/instances//// //`!@#$%^&*()=+/0123456789/[]\\;\',<>?:"{}|/////abcdefghijklmnopqrstuvwxyz//ABCDEFGHIJKLMNOPQRSTUVWXYZ/-_.~:GET/'

        signer.signV3(method=self.method, region=self.region, host=self.host, path=ori_path, query=self.query,
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=92e4897d2a74a899399f5443615ddf110978363b9097932e522e079e6eb5f65b'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_path_encode(self):
        signer = Signer(self.logger)
        ori_path = '/v1/regions/cn-north-1/instances/%20/%60%21%40%23%24%25%5E%26%2A%28%29%3D%2B/0123456789/%5B%5D%5C%5C%3B%27%2C%3C%3E%3F%3A%5C%22%7B%7D%7C/abcdefghijklmnopqrstuvwxyz/ABCDEFGHIJKLMNOPQRSTUVWXYZ/-_.~%3AGET'

        signer.signV3(method=self.method, region=self.region, host=self.host, path=ori_path, query=self.query,
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=027b5bbd35956b84b8773eb450c0405cb4e424eab13f64828926ee41838c48d0'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_path_encodeIncludeEncodedSlashes(self):
        signer = Signer(self.logger)
        ori_path = '%2Fv1%2Fregions%2F%2F%2Fcn-north-1%2Finstances'

        signer.signV3(method=self.method, region=self.region, host=self.host, path=ori_path, query=self.query,
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=33df199719f9edc6de860e6b53c61d4824e1f389e6030fd37ddc977fda29e467'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_path_partEncode(self):
        signer = Signer(self.logger)
        ori_path = '/v1%2Fregions/cn-north-1%2F%2F%2Finstances'
        signer.signV3(method=self.method, region=self.region, host=self.host, path=ori_path, query=self.query,
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=33df199719f9edc6de860e6b53c61d4824e1f389e6030fd37ddc977fda29e467'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_path_wrongPercentEncode(self):
        signer = Signer(self.logger)
        ori_path = '/v1/%2/%2f/%2b%f'
        signer.signV3(method=self.method, region=self.region, host=self.host, path=ori_path, query=self.query,
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=6610271450ea321baab326f8debc51a2e4dd7e73b04200275a1d9b3897045caf'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_path_partEncode_includeSpecialChar(self):
        signer = Signer(self.logger)
        ori_path = '/v1%2Fregions/cn-north-1%2F%2F%2Finstances/ + /+/ +/+ /%2B%20%2B%2F%2F'
        signer.signV3(method=self.method, region=self.region, host=self.host, path=ori_path, query=self.query,
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=7286237483a7fcc51ff7621c9a5c586a0ec85fd06cbf91c20adde2ec3b5e4d97'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_query_nullKey(self):
        signer = Signer(self.logger)
        query = '?=a&a=a'
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=query[1:],
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=43efb5fb00e86faf35d8bf0bed3b72e84cfc98ee4754065e29c3caa7bcaa12cb'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_query_nullKeyAndValue(self):
        signer = Signer(self.logger)
        query = '?=&a=a'
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=query[1:],
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=43efb5fb00e86faf35d8bf0bed3b72e84cfc98ee4754065e29c3caa7bcaa12cb'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_query_repeatQueryquery(self):
        signer = Signer(self.logger)
        query = '?aa=aa&aa%3Daa=&aa=aa%3D&aa=&aa=aaa&aaa=aaa&aaa=aa&aaa=a&ab=aa&ab=aa&cc=&cc=&bb=aa&bb='
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=query[1:],
                    headers=self.header, data='', credential=self.credential,
                    security_token='', service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=8ccc3c9af11e964b3c5d6020d2af49e97e27fbb23e2b8f57bdc84815e471d54b'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_query_specialCharacters0(self):
        signer = Signer(self.logger)
        query = '?special key=/ /`!@#$%^*()+/0123456789/[]\\;\',<>?:"{}|/abcdefghijklmnopqrstuvwxyz/ABCDEFGHIJKLMNOPQRSTUVWXYZ/-_.~&/ /`!@#$%^*()+/0123456789/[]\\;\',<>?:"{}|/abcdefghijklmnopqrstuvwxyz/ABCDEFGHIJKLMNOPQRSTUVWXYZ/-_.~=special value'
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=query[1:],
                    headers=self.header, data="", credential=self.credential,
                    security_token="", service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=684a4397896f81eaefbba29c42be66080b32993dce700e1647608a64595fd655'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_query_specialCharacters2(self):
        signer = Signer(self.logger)
        query = {}
        query['nullValue'] = ''
        query[''] = 'nullKey'
        query['specialValue'] = '&&==&==&&=&='
        query['&&==&==&&=&='] = 'specialKey'

        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=query,
                    headers=self.header, data="", credential=self.credential,
                    security_token="", service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=cc1b199ef770ffc179b3915b9cefa83024bda9d88638c19fe079292de5b91546'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_query_partEncode(self):
        signer = Signer(self.logger)
        query = '? =blank&%20=blank&+= 2&%2b= 1&blank= &blank=+&blank=%20'
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=query[1:],
                    headers=self.header, data="", credential=self.credential,
                    security_token="", service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=78c0a4db84050d773533c78c1a0f73bf974faf5df881e39b18c3e0de8110324e'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_query_wrongPercentEncode(self):
        signer = Signer(self.logger)
        query = '? =blank&%2=blank&+=jia0&%2b=jia1&%2B=jia2&blank= %2b%2f%2/&blank=+&%2/blank=%0%f'
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=query[1:],
                    headers=self.header, data="", credential=self.credential,
                    security_token="", service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=972987a6f95be456935cde8be8f106114e2ad27465a507644e61f021a98a7218'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_query_chinese(self):
        signer = Signer(self.logger)
        query = '?中文参数=中文参数值'
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=query[1:],
                    headers=self.header, data="", credential=self.credential,
                    security_token="", service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=7e3094d23adde49fcc99b7d0de911d7ecaa7767590edd57769d7bdbaca919276'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_head_one_blank(self):
        signer = Signer(self.logger)
        self.header['x-jdcloud-nonce'] = ' X-Jdcloud- -Nonce '
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=self.query,
                    headers=self.header, data="", credential=self.credential,
                    security_token="", service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=5d955d1de475eac2b4378473ca0adce8fddd13f45d2be53bc2ffb6eee6450ba4'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_head_more_blank(self):
        signer = Signer(self.logger)
        self.header['x-jdcloud-nonce'] = '  X-Jdcloud-  -Nonce  '
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=self.query,
                    headers=self.header, data="", credential=self.credential,
                    security_token="", service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=a03bb8d755cb93e4d8846fe5fcad180f319fa50356f63e8afdc749bd1a95695f'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_head_multiValues(self):
        signer = Signer(self.logger)
        self.header['x-jdcloud-nonce'] = ["aaa"]
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=self.query,
                    headers=self.header, data="", credential=self.credential,
                    security_token="", service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=12ed9fbf2f8ebe6afcdd23853c9e58f37642f8a0361765557d2e4915f1e995e4'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_head_special_characters0(self):
        signer = Signer(self.logger)
        self.header['x-jdcloud-nonce'] = '/`!@#$%^&*()=+/0123456789/[]\\;\',<>?:"{}|/abcdefghijklmnopqrstuvwxyz/ABCDEFGHIJKLMNOPQRSTUVWXYZ/-_.~'
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=self.query,
                    headers=self.header, data="", credential=self.credential,
                    security_token="", service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=9046b11889b993a808fccf1322f7f04e7e5a7e0cc22d8b65e9986a8aab986ad7'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)

    def testSign_head_special_characters1(self):
        signer = Signer(self.logger)
        self.header['x-jdcloud-nonce'] = ' \\n  as\\r\\n \\r df\\r\\n   '
        signer.signV3(method=self.method, region=self.region, host=self.host, path=self.ori_path, query=self.query,
                    headers=self.header, data="", credential=self.credential,
                    security_token="", service=self.service_name)
        print(self.header.get(const.JDCLOUD_AUTH))
        true_sign = 'JDCLOUD3-HMAC-SHA256 Credential=ak/20190917/cn-north-1/apigatewaytestproductline/jdcloud3_request, SignedHeaders=content-type;host;x-jdcloud-date;x-jdcloud-nonce, Signature=b30037126cdc4385e957e24e6d73ea28a8fb66f71ee68b8f60de12d3292d19c6'
        print(true_sign)
        self.assertTrue(self.header.get(const.JDCLOUD_AUTH) == true_sign)
