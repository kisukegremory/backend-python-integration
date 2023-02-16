from chalice import Chalice

app = Chalice(app_name='ConsumerLambda')


@app.on_sqs_message(queue='elegibility')
def consumer(event):
    for record in event:
        body = record.body
        print("We received a message %s" % body)