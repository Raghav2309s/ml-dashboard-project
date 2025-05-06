import pandas as pd
import io
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def analyze_csv_and_train_model(file_bytes):
    df = pd.read_csv(io.BytesIO(file_bytes))

    if df.shape[1] < 2:
        return {"error": "Not enough columns"}

    target_col = df.columns[-1]

    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    X = pd.get_dummies(X)
    if y.dtype == 'object':
        y = pd.factorize(y)[0]

    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier()
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        accuracy = accuracy_score(y_test, preds)

        return {
            "summary": {
                "rows": df.shape[0],
                "columns": df.shape[1],
                "target_column": target_col
            },
            "model": {
                "algorithm": "RandomForestClassifier",
                "accuracy": round(accuracy, 4)
            }
        }
    except Exception as e:
        return {"error": str(e)}
