import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Load API Key from environment variables
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def perform_eda(df: pd.DataFrame):
    summary = df.describe().to_dict()
    missing_values = df.isnull().sum().to_dict()

    # Generate a correlation heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    heatmap_path = "heatmap.png"
    plt.savefig(heatmap_path)
    plt.close()

    # Generate Insights using LLM
    insights = generate_insight(summary, missing_values)

    return {
        "summary": summary,
        "missing_values": missing_values,
        "heatmap": heatmap_path,
        "insights": insights
    }

def generate_insight(summary, missing_values):
    if not OPENAI_API_KEY:
        return "Error: OpenAI API key is missing."

    prompt = f"""
    Given the following dataset summary statistics and missing values report, generate a concise data analysis report:

    Summary Statistics:
    {summary}

    Missing Values:
    {missing_values}

    Provide insights about data trends, potential issues, and recommendations.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        api_key=OPENAI_API_KEY
    )

    return response["choices"][0]["message"]["content"]
