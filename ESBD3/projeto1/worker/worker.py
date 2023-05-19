import sys
import time
import zmq
from model_pipeline import *
import os



if __name__ == '__main__':
    
    ZMQ_WVENTILATOR_ADDRESS = os.environ["ZMQ_WVENTILATOR_ADDRESS"]
    ZMQ_WSINK_ADDRESS = os.environ["ZMQ_WSINK_ADDRESS"]
    
    context = zmq.Context()

    # Socket to receive messages on
    receiver = context.socket(zmq.PULL)
    receiver.connect(ZMQ_WVENTILATOR_ADDRESS)
    #receiver.connect("tcp://*:5557")

    # Socket to send messages to
    sender = context.socket(zmq.PUSH)
    
    sender.connect(ZMQ_WSINK_ADDRESS)
    #sender.connect("tcp://*:5558")

    print('Loading dataset...')
    train = importar_dados('/dados/KDDTrain+.txt')
    test = importar_dados('/dados/KDDTest+.txt')
    print('Transforming dataset...')
    X_train , y_train = transformar_dados(train)
    X_test , y_test   = transformar_dados(test)
    print('Normalizing dataset...')
    X_train , X_test = equalizar_dataframes(X_train , X_test)
    print('Waiting ...')
    
    while True:
    #  Wait for next request from client
        params = receiver.recv_json()
        print(f"Received request: {params}")

        #  Do some 'work'
        model_worker = model_train(X_train , y_train, params)
        print('Predicting test sample...')
        predictions = model_worker.predict(X_test)
        acc = accuracy_score(y_test, predictions)
        print('Saving Object...')
        with open('/dados/' + 'worker_model_' + str(params) + '.pickle', 'wb') as handle:
            pickle.dump(model_worker, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print('DONE')
        # Send results to sink
        sender.send_json({'model':params, 'accuracy':acc})
       