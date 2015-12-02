# This script created a queue
#
# Author - Paul Doyle Nov 2015
#
#
import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError
import sys
import urllib2

response = urllib2.urlopen('http://ec2-52-30-7-5.eu-west-1.compute.amazonaws.com:81/key')
html=response.read()
result = html.split(':')

access_key_id = result[0]
secret_access_key = result[1]

conn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
queueName = sys.argv[1]
try:
    rs = conn.create_queue(queueName)
    print('queue ' + queueName + ' is now created')
except Exception, e:
    print(e)


