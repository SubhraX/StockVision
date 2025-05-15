
# 📈 StockVision

StockVision is a full-stack stock prediction web app built with **React** (frontend) and **FastAPI** (backend). It allows users to view stock charts and receive predictions via a machine learning model.

---

## 📁 Project Structure

```
StockVision/
│
├── stock-frontend/           # React frontend
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── StockChart.js
│   │   └── ...
│   ├── package.json
│   └── ...
│
└── stock-predictor-app/      # FastAPI backend
    ├── main.py
    ├── venv/
    └── ...
```

---

## ⚙️ Prerequisites

Before running the app, ensure the following are installed:

- [Node.js](https://nodejs.org/) (v14+)
- [Python](https://www.python.org/) (v3.8+)
- [Git](https://git-scm.com/)

---

## 🚀 Getting Started

You'll need **two terminals** open to run both the frontend and backend servers.

---

### 🟡 1. Backend Setup (FastAPI)

#### Navigate to the backend folder:
```powershell
cd stock-predictor-app
```

#### Create and activate a virtual environment:
```powershell
python -m venv venv
venv\Scripts\Activate.ps1   # Use `source venv/bin/activate` on Linux/macOS
```

#### Install dependencies:
```powershell
pip install fastapi uvicorn numpy pandas scikit-learn
```

#### (Optional) Install CORS middleware if using frontend:
```powershell
pip install fastapi[all]
```

#### Run the backend server:
```powershell
uvicorn main:app --reload
```

This starts the API at: [http://localhost:8000](http://localhost:8000)

---

### 🔵 2. Frontend Setup (React)

#### Navigate to the frontend folder:
```powershell
cd stock-frontend
```

#### Install Node.js dependencies:
```powershell
npm install
```

#### Start the development server:
```powershell
npm start
```

This starts the frontend at: [http://localhost:3000](http://localhost:3000)

---

## 🔁 How It Works

1. User opens the frontend React interface.
2. Enters a stock symbol or relevant input.
3. The React app sends a `POST` request to the FastAPI backend.
4. The backend processes the input and returns predictions.
5. The frontend displays prediction results and/or visual charts.

---

## 📦 Example API (FastAPI)

In `main.py`:
```python
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict to http://localhost:3000
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StockInput(BaseModel):
    symbol: str

@app.post("/predict")
def predict(input: StockInput):
    # Placeholder logic for stock prediction
    return {"symbol": input.symbol, "prediction": "up"}
```

---

## 📈 Example Frontend Usage (React)

In `StockChart.js` or similar:
```javascript
fetch("http://localhost:8000/predict", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ symbol: "AAPL" })
})
.then(res => res.json())
.then(data => {
  console.log("Prediction:", data.prediction);
});
```

---

## 🧪 Running Tests

- Frontend:
  ```bash
  npm test
  ```

- Backend:
  Add test cases using `pytest` or `unittest` and run:
  ```bash
  pytest
  ```

---

## 📄 License

This project is licensed under the MIT License. See `LICENSE` for more details.

---

## 🙋‍♂️ Contributors

- You!

---

## 🧠 Future Improvements

- Integrate real-time stock data
- Improve ML model accuracy
- Deploy to the cloud (e.g., Render, Vercel)

---
