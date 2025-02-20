from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io
from eda import perform_eda
from ml_model import suggest_model

app = FastAPI()

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    df = pd.read_csv(io.StringIO(contents.decode("utf-8")))
    df = df.apply(pd.to_numeric, errors='coerce')  # Convert columns to numeric, setting non-numeric values to NaN
    df.fillna(0, inplace=True)
    eda_results = perform_eda(df)
    model_suggestion = suggest_model(df)

    return {
        "eda": eda_results,
        "model": model_suggestion,
        "insights": eda_results["insights"],  # Include insights in response
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
