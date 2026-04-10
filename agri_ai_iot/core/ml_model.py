import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import joblib
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
DATASET_PATH = os.path.join(BASE_DIR, "dataset.csv")


def train_model():

    data = pd.read_csv(DATASET_PATH)

    # Convert yield to classification
    data['yield_class'] = data['yield'].apply(lambda x: 1 if x > 4 else 0)

    X = data[['soil_moisture','temperature','humidity',
              'nitrogen','phosphorus','potassium']]
    y = data['yield_class']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    joblib.dump(model, MODEL_PATH)

    return accuracy, cm


# ✅ Prediction Function
def predict(data_dict):

    if not os.path.exists(MODEL_PATH):
        train_model()

    model = joblib.load(MODEL_PATH)

    df = pd.DataFrame([data_dict])
    prediction = model.predict(df)

    return prediction[0]


# ✅ Feature Importance Function (ADD THIS)
def get_feature_importance():

    if not os.path.exists(MODEL_PATH):
        train_model()

    model = joblib.load(MODEL_PATH)

    features = ['soil_moisture','temperature','humidity',
                'nitrogen','phosphorus','potassium']

    importance = model.feature_importances_

    return dict(zip(features, importance))