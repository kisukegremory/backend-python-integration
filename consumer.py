import json
from models.Elegibility import Elegibility
from services import queues


for message in queues.elegibility.receive_messages(
            MessageAttributeNames=['All'],
            MaxNumberOfMessages=10,
            WaitTimeSeconds=5
    ):
    model = Elegibility(**json.loads(message.body))
    print(model.json())
    message.delete()
    print("Deleted message: %s", message.message_id)
