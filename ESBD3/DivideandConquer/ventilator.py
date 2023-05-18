import zmq
import random
import time


context = zmq.Context()

# Socket to send messages on
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

# Socket with direct access to the sink: used to synchronize start of batch
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

print("Press Enter when the workers are ready: ")
_ = input()
print("Sending tasks to workers...")

# The first message is "0" and signals start of batch
sink.send(b'0')

# Initialize random number generator
random.seed()

#  Do 10 requests, waiting each time for a response
for request in range(10):

    print(f"Sending request {request} ...")
    sender.send_json({'min_samples_leaf': request+1 ,'n_estimators': 10*(request+1)})
