import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor

def suggest_model(df: pd.DataFrame):
    if df.isnull().values.any():
        return "Please clean missing values before selecting a model."
    
    target = df.columns[-1]  # Assuming last column is the target
    X = df.drop(columns=[target])
    y = df[target]
    
    if y.nunique() <= 10:  # Classification if target has few unique values
        model = RandomForestClassifier()
        model_type = "Classification"
    else:
        model = RandomForestRegressor()
        model_type = "Regression"
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    
    return {"model": model_type, "accuracy": score}
