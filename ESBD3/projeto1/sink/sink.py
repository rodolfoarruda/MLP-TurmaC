import sys
import time
import zmq
import os


ZMQ_SINK_ADDRESS = os.environ["ZMQ_SINK_ADDRESS"]

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind(ZMQ_SINK_ADDRESS)


# Wait for start of batch
s = receiver.recv()

# Start our clock now
tstart = time.time()

 #  Get the reply.
 
for request in range(100): 
    message = receiver.recv()
    print(f"Received reply [ {message} ]")

# Calculate and report duration of batch
tend = time.time()
print(f"Total elapsed time: {(tend-tstart)*1000} msec")