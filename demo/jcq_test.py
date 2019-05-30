import unittest
from jdcloud_sdk.core.credential import Credential
from jdcloud_sdk.services.jcq.client.JcqClient import JcqClient
from jdcloud_sdk.services.jcq.apis.DescribeAccessPointRequest import *
from jdcloud_sdk.services.jcq.apis.DescribeMessageRequest import *
from jdcloud_sdk.services.jcq.models.AccessPoint import AccessPoint
from jdcloud_sdk.services.jcq.models.Message import Message
from jdcloud_sdk.services.jcq.apis.DescribeMessagesRequest import *
from jdcloud_sdk.services.jcq.apis.DescribeTopicRequest import *
from jdcloud_sdk.services.jcq.models.Topic import Topic
from jdcloud_sdk.services.jcq.apis.DescribeTopicsRequest import *
from jdcloud_sdk.services.jcq.apis.CreateTopicRequest import *
from jdcloud_sdk.services.jcq.apis.DeleteTopicRequest import *
from jdcloud_sdk.services.jcq.apis.CreateSubscriptionRequest import *
from jdcloud_sdk.services.jcq.apis.DeleteSubscriptionRequest import *
from jdcloud_sdk.services.jcq.apis.DescribeSubscriptionRequest import *
from jdcloud_sdk.services.jcq.models.Subscription import Subscription
from jdcloud_sdk.services.jcq.apis.DescribeSubscriptionsRequest import *
from jdcloud_sdk.services.jcq.apis.CleanMessagesRequest import *
from jdcloud_sdk.services.jcq.apis.ResetConsumeOffsetRequest import *
from jdcloud_sdk.services.jcq.apis.DescribeDeadLetterNumbersRequest import *
from jdcloud_sdk.services.jcq.apis.DescribeDeadLetterNumbersWithTopicRequest import *
from jdcloud_sdk.services.jcq.models.DeadLetterNumber import DeadLetterNumber
from jdcloud_sdk.services.jcq.apis.DeleteDeadLettersRequest import *
from jdcloud_sdk.services.jcq.apis.ListDeadLettersRequest import *
from jdcloud_sdk.services.jcq.models.DeadLetter import DeadLetter
from jdcloud_sdk.services.jcq.apis.ResendDeadLettersRequest import *
from jdcloud_sdk.services.jcq.apis.AddPermissionRequest import *
from jdcloud_sdk.services.jcq.apis.DescribePermissionRequest import *
from jdcloud_sdk.services.jcq.apis.RemovePermissionRequest import *
from jdcloud_sdk.services.jcq.models.Permission import Permission
from jdcloud_sdk.services.jcq.apis.DescribeConsumerGroupIdsRequest import *


class JcqTest(unittest.TestCase):
    def setUp(self):
        access_key = 'ak'
        secret_key = 'sk'
        self.credential = Credential(access_key, secret_key)
        self.client = JcqClient(self.credential)

    # get access point
    def testDescribeAccessPoint(self):
        request_param = DescribeAccessPointParameters('region_id', 'topic_name')
        request = DescribeAccessPointRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        # sdkAddress sdk access point
        # httpAddress httpProxy access point
        access_point = AccessPoint(resp.result['accessPoint']['sdkAddress'], resp.result['accessPoint']['httpAddress'])

    # get message by message id
    def testDescribeMessageRequest(self):
        request_param = DescribeMessageParameters('region_id', 'topic_name', 'message_id')
        request = DescribeMessageRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        message_res = resp.result['message']
        message = Message(message_res['messageId'], message_res['body'], message_res['tag'], message_res['properties'],
                          message_res['storeTime'])

    # batch get message
    def testDescribeMessagesRequest(self):
        request_param = DescribeMessagesParameters('region_id', 'topic_name', '2019-05-21T16:00:00Z',
                                                   '2019-05-22T16:00:00Z')
        request = DescribeMessagesRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        res_list = resp.result['messages']
        messages = []
        for msg in res_list:
            messages.append(Message(msg['messageId'], msg['body'], msg['tag'], msg['properties'],
                                    msg['storeTime']))

    # create topic
    def testCreateTopicRequest(self):
        request_param = CreateTopicParameters('region_id', 'topic_name''normal')
        request = CreateTopicRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    # delete topic
    def testDeleteTopicRequest(self):
        request_param = DeleteTopicParameters('region_id', 'topic_name')
        request = DeleteTopicRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    # query topic
    def testDescribeTopicRequest(self):
        request_param = DescribeTopicParameters('region_id', 'topic_name')
        request = DescribeTopicRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        topic_res = resp.result['topic']
        topic = Topic(topic_res['topicId'], topic_res['topicName'], topic_res['description'], topic_res['createTime'],
                      topic_res['lastUpdateTime'], topic_res['topicStatus'], topic_res['subscriptionCount'],
                      topic_res['messageLifeTimeInHours'], topic_res['topicConfig'], topic_res['own'],
                      topic_res['authorizedPermission'],
                      topic_res['tags'])

    # batch query topic
    def testDescribeTopicsRequest(self):
        request_param = DescribeTopicsParameters('region_id')
        request = DescribeTopicsRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        resp_list = resp.result['topics']
        topics = []
        for topic_res in resp_list:
            topics.append(
                Topic(topic_res['topicId'], topic_res['topicName'], topic_res['description'], topic_res['createTime'],
                      topic_res['lastUpdateTime'], topic_res['topicStatus'], topic_res['subscriptionCount'],
                      topic_res['messageLifeTimeInHours'], topic_res['topicConfig'], topic_res['own'],
                      topic_res['authorizedPermission'],
                      topic_res['tags']))

    # create subscription
    def testCreateSubscriptionRequest(self):
        request_param = CreateSubscriptionParameters('region_id', 'topic_name', 'consumer_group_id')
        request = CreateSubscriptionRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    # delete subscription
    def testDeleteSubscriptionRequest(self):
        request_param = DeleteSubscriptionParameters('regiond_id', 'topic_name', 'consumer_group_id')
        request = DeleteSubscriptionRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    # query subscription
    def testDescribeSubscriptionRequest(self):
        request_param = DescribeSubscriptionParameters('regiond_id', 'topic_name', 'consumer_group_id')
        request = DescribeSubscriptionRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        sub_res = resp.result['subscription']
        subscription = Subscription(sub_res['consumerGroupId'], sub_res['endPoint'],
                                    sub_res['messageInvisibleTimeInSeconds'], sub_res['subscriptionType'],
                                    sub_res['tags'], sub_res['dlqEnable'], sub_res['maxRetryTimes'],
                                    sub_res['createTime'], sub_res['lastUpdateTime'], sub_res['consumerNumbers'])

    # query subscriptions
    def testDescribeSubscriptionsRequest(self):
        request_param = DescribeSubscriptionsParameters('region_id', 'topic_name')
        request = DescribeSubscriptionRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        sub_list = resp.result['subscriptions']
        subscriptions = []
        for sub_res in sub_list:
            subscriptions.append(Subscription(sub_res['consumerGroupId'], sub_res['endPoint'],
                                              sub_res['messageInvisibleTimeInSeconds'], sub_res['subscriptionType'],
                                              sub_res['tags'], sub_res['dlqEnable'], sub_res['maxRetryTimes'],
                                              sub_res['createTime'], sub_res['lastUpdateTime'],
                                              sub_res['consumerNumbers']))

    # reset consume offset
    def testResetConsumeOffsetRequest(self):
        request_param = ResetConsumeOffsetParameters('region_id', 'topic_name', 'consume_group_id',
                                                     '2019-05-21T16:00:00Z')
        request = ResetConsumeOffsetRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    # reset consume offset to the latest
    def testCleanMessagesRequest(self):
        requst_param = CleanMessagesParameters('region_id', 'topic_name', 'consume_group_id')
        request = CleanMessagesRequest(requst_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    # query dead letter
    def testDescribeDeadLetterNumbersRequest(self):
        request_param = DescribeDeadLetterNumbersParameters('region_id')
        request_param.setConsumerGroupId('consume_group_id')
        request = DescribeDeadLetterNumbersRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        result = resp.result['deadLetterNumbers']
        dead_letter_numbers = []
        for dead_letter in result:
            dead_letter_numbers.append(
                DeadLetterNumber(dead_letter['topicId'], dead_letter['topicName'], dead_letter['consumerGroupId'],
                                 dead_letter['deadLetterNumber']))

    # query dead letter by topic
    def testDescribeDeadLetterNumbersWithTopicRequest(self):
        request_param = DescribeDeadLetterNumbersWithTopicParameters('region_id', 'topic_name')
        request = DescribeDeadLetterNumbersWithTopicRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        result = resp.result['deadLetterNumbers']
        dead_letter_numbers = []
        for dead_letter in result:
            dead_letter_numbers.append(
                DeadLetterNumber(dead_letter['topicId'], dead_letter['topicName'], dead_letter['consumerGroupId'],
                                 dead_letter['deadLetterNumber']))

    # delete dead letter
    def testDeleteDeadLettersRequest(self):
        request_param = DeleteDeadLettersParameters('region_id', 'topic_name', 'consumer_group_id')
        request = DeleteDeadLettersRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        message_ids = resp.result['messageIds']

    # query dead letter
    def testListDeadLettersRequest(self):
        request_param = ListDeadLettersParameters('region_id', 'topic_name', 'consumer_group_id',
                                                  '2019-05-21T16:00:00Z', '2019-05-22T16:00:00Z')

        request = ListDeadLettersRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        dead_letters = []
        dead_letters_res = resp.result['deadLetters']
        for dead_letter in dead_letters_res:
            dead_letters.append(DeadLetter(dead_letter['messageId'], dead_letter['expireTime']))

    # resend dead letter
    def testResendDeadLettersRequest(self):
        request_param = ResendDeadLettersParameters('region_id', 'topic_name', 'consumer_group_id')
        request = ResendDeadLettersRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        message_ids = resp.result['messageIds']

    # query permission
    def AddPermissionRequest(self):
        request_param = AddPermissionParameters('region_id', 'topic_name', 'PUB', 'user_id')
        request = AddPermissionRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    # query permissions
    def DescribePermissionRequest(self):
        request_param = DescribePermissionParameters('region_id', 'topic_name')
        request = DescribePermissionRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        permissions = []
        for permission in resp.result['permissions']:
            permissions.append(Permission(permission['userId'], permission['permission']))

    # delete permission
    def testRemovePermissionRequest(self):
        request_param = RemovePermissionParameters('region_id', 'topic_name', 'PUB', 'user_id')
        request = RemovePermissionRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)

    # query consumer group
    def testDescribeConsumerGroupIdsRequest(self):
        request_param = DescribeConsumerGroupIdsParameters('region_id')
        request = DescribeConsumerGroupIdsRequest(request_param)
        resp = self.client.send(request)
        self.assertTrue(resp.error is None)
        consumer_group_ids = resp.result['consumerGroupIds']
