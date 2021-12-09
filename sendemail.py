import logging
import time
import boto3 
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
 
sns_client = boto3.client('sns', verify=False) #Create client to connect to aws sns



#Creates a topic in SNS for us to use for alerts 
def create_topic(name):
    """
    Creates a notification topic.

    :param name: The name of the topic to create.
    :return: The newly created topic.
    """

    try:
        topic = sns_client.create_topic(Name=name)
        logger.info("Created topic %s with ARN %s.", name, topic['TopicArn'])

    except ClientError:
        logger.exception("Couldn't create topic %s.", name)
        raise
    else:
        return topic


#Subscribe to the topic 
def subscribe(topic, protocol, endpoint):
    """
    :param topic: The topic to subscribe to.
    :param protocol: The protocol of the endpoint, such as 'sms' or 'email'.
    :param endpoint: The endpoint that receives messages, such as a phone number
                     (in E.164 format) for SMS messages, or an email address for
                     email messages.
    :return: The newly added subscription.
    """
    try:
        subscription = sns_client.subscribe(
            TopicArn=topic, Protocol=protocol, Endpoint=endpoint, ReturnSubscriptionArn=True)
        logger.info("Subscribed %s %s to topic %s.", protocol, endpoint, topic)
    except ClientError:
        logger.exception(
            "Couldn't subscribe %s %s to topic %s.", protocol, endpoint, topic)
        raise
    else:
        return subscription
#Publish amessage to the email we're subscribed to
def publishmessage(topicArn, doorOpen):

    if(doorOpen == 1):
        sns_client.publish(TopicArn=topicArn,
             Message="A package is being entered into the crate",
             Subject="DOOR ALERT")

    else:
        sns_client.publish(TopicArn=topicArn,
             Message="Barcode will not open for invalid tracking numbers",
             Subject="DOOR ALERT")

#Main Function
if __name__ == '__main__':                             


    topic_name = f'Delivery-Alert'                   #Create the topic name
    protocol = 'email'
    endpoint = 'brown.ennis21@gmail.com'
    topic_arn='arn:aws:sns:us-west-1:862742272774:Delivery-Alert'
    door_open = 1 

    '''Create a topic'''
    #print(f"Creating topic {topic_name}.")
    #topic = create_topic(topic_name)

    '''Subsribe to the topic'''
    #print("Subscribing to the topic")
    #subscription = subscribe(topic_arn, protocol, endpoint)

    '''the f-string format the sring we want to read in the print statement 
       The f or F in front of strings tell Python to look at the values inside {} and 
       substitute them with the variables values if exists.'''
    print(f"Sending a message to {endpoint}. ")  
    publishmessage(topic_arn, door_open)