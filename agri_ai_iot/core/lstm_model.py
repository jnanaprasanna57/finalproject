import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import joblib
import os

MODEL_PATH = "core/lstm_model.h5"
SCALER_PATH = "core/scaler.save"

def train_lstm():
    data = pd.read_csv("dataset.csv")
    series = data['yield'].values.reshape(-1,1)

    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(series)

    X, y = [], []
    for i in range(3, len(scaled)):
        X.append(scaled[i-3:i])
        y.append(scaled[i])

    X, y = np.array(X), np.array(y)

    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=(X.shape[1],1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=50, verbose=0)

    model.save(MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)
from tensorflow.keras.models import load_model

def predict_future(last_values):
    model = load_model(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    last_scaled = scaler.transform(np.array(last_values).reshape(-1,1))
    last_scaled = last_scaled.reshape(1, len(last_values), 1)

    pred_scaled = model.predict(last_scaled)
    prediction = scaler.inverse_transform(pred_scaled)

    return prediction[0][0]
def feature_importance_view(request):
    importance = get_feature_importance()

    features = list(importance.keys())
    values = list(importance.values())

    plt.figure()
    plt.bar(features, values)
    plt.xticks(rotation=45)
    plt.title("Feature Importance")

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graph = base64.b64encode(image_png).decode('utf-8')

    return render(request, 'admin/feature_importance.html', {'graph': graph})
