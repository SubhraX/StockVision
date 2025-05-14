# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import yfinance as yf
import numpy as np
import datetime
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM, Bidirectional

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/predict/{ticker}")
def predict(ticker: str):
    end_date = datetime.datetime.today()
    start_date = end_date - datetime.timedelta(days=100)
    stock_data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'), end=end_date.strftime('%Y-%m-%d'))

    if stock_data.empty:
        return {"error": "No data found"}

    stock_prices = stock_data['Close'].values.reshape(-1, 1)
    dates = stock_data.index.strftime('%Y-%m-%d').tolist()

    # Last 60 days for actual chart
    recent_prices = stock_prices[-60:].flatten().tolist()
    recent_dates = dates[-60:]

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(stock_prices)

    X, y = [], []
    for i in range(60, len(scaled_data)):
        X.append(scaled_data[i - 60:i, 0])
        y.append(scaled_data[i, 0])
    X = np.array(X).reshape(-1, 60, 1)
    y = np.array(y)

    model = Sequential([
        Bidirectional(LSTM(50, return_sequences=True), input_shape=(60, 1)),
        Dropout(0.2),
        Bidirectional(LSTM(50)),
        Dropout(0.2),
        Dense(25),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(X, y, epochs=3, batch_size=32, verbose=0)

    input_seq = scaled_data[-60:].reshape(1, 60, 1)
    future_preds = []
    for _ in range(30):
        pred = model.predict(input_seq, verbose=0)[0, 0]
        future_preds.append(pred)
        input_seq = np.append(input_seq[:, 1:, :], [[[pred]]], axis=1)

    predicted_prices = scaler.inverse_transform(np.array(future_preds).reshape(-1, 1)).flatten()
    future_dates = [(stock_data.index[-1] + datetime.timedelta(days=i)).strftime('%Y-%m-%d') for i in range(1, 31)]

    return {
        "recent_dates": recent_dates,
        "recent_prices": recent_prices,
        "dates": future_dates,
        "predictions": predicted_prices.tolist()
    }
