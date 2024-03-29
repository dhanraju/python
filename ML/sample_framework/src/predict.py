import os
import pandas as pd
from sklearn import ensemble
from sklearn import preprocessing
from sklearn import metrics
import joblib

from . import dispatcher

TRAINING_DATA = os.environ.get("TRAINING_DATA")
TEST_DATAFOLD = os.environ.get("TEST_DATA")
MODEL = os.environ.get("MODEL")

if __name__ == "__main__":
    df = pd.read_csv(TRAINING_DATA)
    train_df = df[df.kfold.isin(FOLD_MAPPING.get(FOLD))]
    valid_df = df[df.kfold==FOLD]

    ytrain = train_df.target.values
    yvalid = valid_df.target.values

    train_df = train_df.drop(["id", "target", "kfold"], axis=1)
    valid_df = valid_df.drop(["id", "target", "kfold"], axis=1)

    valid_df = valid_df[train_df.columns]

    label_encoders = []

    for c in train_df.columns:
        lbl = preprocessing.LabelEncoder()
        lbl.fit(train_df[c].values.tolist() + valid_df[c].values.tolist())
        train_df.loc[:, c] = lbl.transform(train_df[c].values.tolist())
        valid_df.loc[:, c] = lbl.transform(valid_df[c].values.tolist())
        label_encoders.append((c, lbl))
    
    # data is ready to train
    clf = dispatcher.MODELS[MODEL]
    # clf = ensemble.RandomForestClassifier(n_estimators=200, n_jobs=-1, verbose=2)
    clf.fit(train_df, ytrain)
    preds = clf.predict_proba(valid_df)[:, 1]
    # print(preds)
    print(metrics.roc_auc_score(yvalid, preds))

    joblib.dump(label_encoders, f"models/{MODEL}_label_encoder.pkl")
    joblib.dump(clf, f"models/{MODEL}.pkl")