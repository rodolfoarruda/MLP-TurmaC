import ast
import json
import pandas as pd
import pickle
import sys

from datetime import datetime
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score


def importar_dados(arquivo):

    feature=["duration","protocol_type","service","flag","src_bytes","dst_bytes","land","wrong_fragment","urgent","hot",
              "num_failed_logins","logged_in","num_compromised","root_shell","su_attempted","num_root","num_file_creations","num_shells",
              "num_access_files","num_outbound_cmds","is_host_login","is_guest_login","count","srv_count","serror_rate","srv_serror_rate",
              "rerror_rate","srv_rerror_rate","same_srv_rate","diff_srv_rate","srv_diff_host_rate","dst_host_count","dst_host_srv_count", 
              "dst_host_same_srv_rate","dst_host_diff_srv_rate","dst_host_same_src_port_rate","dst_host_srv_diff_host_rate","dst_host_serror_rate",
              "dst_host_srv_serror_rate","dst_host_rerror_rate","dst_host_srv_rerror_rate","label","difficulty"]

    df = pd.read_csv(arquivo, sep=',', header=None,names=feature)
    
    return df


def transformar_dados(df):
    
    df.drop(['difficulty'],axis=1,inplace=True)
    df = pd.get_dummies(df, columns=['protocol_type'], prefix="dmy", prefix_sep="_" )
    df = pd.get_dummies(df, columns=['service'], prefix="dmy", prefix_sep="_")
    df = pd.get_dummies(df, columns=['flag'], prefix="dmy", prefix_sep="_")
    
    y = df['label']
    X = df.drop(columns=['label'])

    return X , y


def equalizar_dataframes(df_train, df_test):


    df_train = df_train.filter(regex='^(dmy_)').fillna(-1)
    df_test = df_test.filter(regex='^(dmy_)').fillna(-1)

    # Testset with same columns trainset

    new_cols = set(df_train.columns) - set(df_test.columns)

    # adicionar colunas faltantes em B e preencher com -1
    for col in new_cols:
        df_test[col] = -1

    # remover colunas de B que não estão presentes em A
    for col in df_test.columns:
        if col not in df_train.columns:
            df_test.drop(columns=[col], inplace=True)

        # reordenar colunas de B para ficar igual a A
        df_test = df_test[df_train.columns].copy()

    return df_train, df_test

def model_train(X,y,params):

    model = make_pipeline(RandomForestClassifier(**params))

    return model.fit(X, y)
