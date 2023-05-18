import time
import zmq
from model_pipeline import *



if __name__ == '__main__':
    
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")


    print('Loading dataset...')
    train = importar_dados('KDDTrain+.txt')
    test = importar_dados('KDDTest+.txt')
    print('Transforming dataset...')
    X_train , y_train = transformar_dados(train)
    X_test , y_test   = transformar_dados(test)
    print('Normalizing dataset...')
    X_train , X_test = equalizar_dataframes(X_train , X_test)
    print('Training model...')
    
    while True:
    #  Wait for next request from client
        params = socket.recv_json()
        print(f"Received request: {params}")

        #  Do some 'work'
        model_worker = model_train(X_train , y_train, params)
        print('Predicting test sample...')
        predictions = model_worker.predict(X_test)
        acc = accuracy_score(y_test, predictions)
        print('Saving Object...')
        with open('worker_model_' + str(params) + '.pickle', 'wb') as handle:
            pickle.dump(model_worker, handle, protocol=pickle.HIGHEST_PROTOCOL)
        print('DONE')
        #  Send reply back to client
        socket.send_json({'model':params, 'accuracy':acc})
