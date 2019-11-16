from __future__ import print_function
  
import json
import boto3
  
print('Loading function')
  
def lambda_handler(event, context):
    recv_msg = json.loads(json.dumps(event))
   
    if recv_msg["Msg_type"] == "data":
       sqs = boto3.resource('sqs')
       queue = sqs.get_queue_by_name(QueueName='my_queue_project_3')
       response = queue.send_message(MessageBody= json.dumps(event))
    elif recv_msg["Msg_type"] == "alert":
        # Print the parsed JSON message to the console; you can view this text in the Monitoring tab in the Lambda console or in the CloudWatch Logs console
        #print('Received event: ', eventText)
        
        # Create an SNS client
        sns = boto3.client('sns')
        
        # Publish a message to the specified topic
        response = sns.publish (
            TopicArn = 'arn:aws:sns:us-east-1:222513434401:project_3_sns_topic',
            Message = json.dumps(event)
            )
            
    
    print(response)
