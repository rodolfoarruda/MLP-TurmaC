import zmq
import random
import time
import os


ZMQ_VENTILATOR_ADDRESS = os.environ["ZMQ_VENTILATOR_ADDRESS"]
ZMQ_WSINK_ADDRESS = os.environ["ZMQ_WSINK_ADDRESS"]

context = zmq.Context()

# Socket to send messages on
sender = context.socket(zmq.PUSH)
sender.bind(ZMQ_VENTILATOR_ADDRESS)

# Socket with direct access to the sink: used to synchronize start of batch
sink = context.socket(zmq.PUSH)
sink.connect(ZMQ_WSINK_ADDRESS)

# The first message is "0" and signals start of batch
sink.send(b'0')

# Initialize random number generator
random.seed()

#  Do 10 requests, waiting each time for a response
for request in range(100):

    print(f"Sending request {request} ...")
    sender.send_json({'min_samples_leaf': request+1 ,'n_estimators': 10*(request+1)})
