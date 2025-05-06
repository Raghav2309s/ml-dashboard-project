# 🧠 ML Dashboard (React + FastAPI)

This is a full-stack machine learning dashboard that allows you to upload a CSV, train a simple model, and display basic insights.

---

## 🚀 Features

- Upload CSV files
- Auto-detect target column
- Train a RandomForestClassifier
- Display dataset summary & model accuracy

---

## 📁 Project Structure

```
ml-dashboard-project/
├── ml-dashboard-backend/
│   ├── main.py
│   ├── requirements.txt
│   └── utils/
│       └── ml_utils.py
└── ml-dashboard-frontend/
    ├── index.html
    ├── package.json
    ├── vite.config.js
    └── src/
        ├── main.jsx
        ├── App.jsx
        └── components/
            └── UploadForm.jsx
```

---

## 🛠️ Local Setup

### 1. Backend (FastAPI)

```bash
cd ml-dashboard-backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Runs at: `http://localhost:8000`

---

### 2. Frontend (React + Vite)

```bash
cd ml-dashboard-frontend
npm install
npm run dev
```

Runs at: `http://localhost:5173`

---

## 🌍 Deployment

### Backend → [Render](https://render.com)
- Push backend to GitHub
- Create new Web Service on Render
- Use `uvicorn main:app --host=0.0.0.0 --port=10000` as start command

### Frontend → [Netlify](https://netlify.com) or [Vercel](https://vercel.com)
- Push frontend to GitHub
- Set build command: `npm run build`
- Publish directory: `dist`

**Important**: Update API URL in `UploadForm.jsx` with your Render backend URL before deploying.

---

## ✅ Example Output

- Rows: 150
- Columns: 5
- Target Column: species
- Model: RandomForestClassifier
- Accuracy: 0.9333

---

## 📄 License

MIT
