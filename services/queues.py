import boto3
sqs = boto3.resource('sqs')
elegibility = sqs.get_queue_by_name(QueueName='elegibility')


