import zmq

from random import randint

context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")



#socket.send_json({'min_samples_leaf': 1,'n_estimators': 100})
#socket.send_string("Hello")

#  Do 10 requests, waiting each time for a response
for request in range(10):


    print(f"Sending request {request} ...")
    socket.send_json({'min_samples_leaf': request+1 ,'n_estimators': 10*(request+1)})


    #  Get the reply.
    message = socket.recv()
    print(f"Received reply [ {message} ]")
