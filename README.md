
# StockVision

StockVision is a full-stack stock price prediction application that uses a FastAPI backend with an BiLSTM-based machine learning model and a React frontend for data visualization.

---

## 🚀 Features

- Predicts future stock prices for any given ticker symbol (e.g., AAPL, TSLA, etc.)
- Uses historical stock data from Yahoo Finance (via yfinance)
- Implements a Bidirectional LSTM model using TensorFlow/Keras
- Frontend visualizes both actual and predicted stock prices using Chart.js with zoom and pan support

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- yfinance
- NumPy, Scikit-learn
- TensorFlow/Keras

### Frontend
- React.js
- Chart.js with zoom plugin
- JavaScript/JSX

---

## 🧪 Project Structure

```
StockVision/
├── stock-frontend/          # React frontend
│   └── src/
│       └── StockChart.js    # Chart component fetching backend predictions
├── stock-predictor-app/     # FastAPI backend
│   ├── main.py              # ML model + API
│   └── venv/                # Python virtual environment
```

---

## 🖥️ Getting Started

### Backend (FastAPI)

1. **Navigate to backend directory**:
```bash
cd stock-predictor-app
```

2. **Activate virtual environment (PowerShell)**:
```powershell
venv\Scripts\Activate.ps1
```

3. **Run the backend server**:
```bash
uvicorn main:app --reload
```

> The API will be live at `http://127.0.0.1:8000`

---

### Frontend (React)

1. **Navigate to frontend directory**:
```bash
cd stock-frontend
```

2. **Install dependencies**:
```bash
npm install
```

3. **Start the development server**:
```bash
npm start
```

> The app will run at `http://localhost:3000`

---

## 🔍 Example Usage

Visit the frontend app and enter a stock ticker (e.g., `AAPL`) to view predictions. The backend fetches the last 100 days of data, trains a model on it, and forecasts the next 30 days.

---

## 📄 License

Apache-2.0 License

---

## 📫 Contact

For any questions or suggestions, please open an issue or contribute to this repository.

