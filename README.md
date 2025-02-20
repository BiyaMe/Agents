# AI-Assisted Data Science Assistant

An interactive AI-powered data science assistant that helps with **data analysis, insights generation, and machine learning model suggestions** through a **FastAPI backend** and **Streamlit frontend**.

---

## 🚀 Features

- 📊 **Upload CSV datasets** for analysis.
- 🔍 **Automated Exploratory Data Analysis (EDA)**.
- 🧠 **AI-generated insights** using OpenAI's LLM.
- 🤖 **Suggested ML models** based on data structure.
- 🌐 **FastAPI backend** for processing and LLM integration.
- 🖥️ **Streamlit frontend** for easy interaction.

---

## 📂 Project Structure
```
AI-agent/
│── backend/
│   │── main.py             # FastAPI backend
│   │── data_analysis.py    # Data processing & EDA functions
│   │── llm_integration.py  # OpenAI API integration
│   │── requirements.txt    # Backend dependencies
│── frontend/
│   │── app.py              # Streamlit frontend
│── .env                    # Environment variables (API keys)
│── README.md               # Project documentation
│── requirements.txt         # Frontend dependencies
```

---

## 🛠️ Setup Instructions

### 1️⃣ Install Dependencies

#### **Backend (FastAPI)**
```bash
cd backend
pip install -r requirements.txt
```

#### **Frontend (Streamlit)**
```bash
cd frontend
pip install -r requirements.txt
```

### 2️⃣ Set Up Environment Variables
Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_actual_api_key_here
```

### 3️⃣ Run the Backend
```bash
cd backend
uvicorn main:app --reload
```

### 4️⃣ Run the Frontend
Open a new terminal and run:
```bash
cd frontend
streamlit run app.py
```

---

## 📌 Usage Guide
1. **Upload a CSV file** via the Streamlit interface.
2. The backend **performs EDA** and returns key insights.
3. The AI **generates data insights** using OpenAI.
4. The system **suggests a machine learning model**.
5. **View the results** on the frontend.

---


## 📌 Extra things
1. To see etra feedbacks you can uncomment the commented codes in the 'app.py'.
2. If you run into trouble when using APIs you can remove the 'not in eda.py
    ```"def generate_insight(summary, missing_values):
            if OPENAI_API_KEY:
                return "Error: OpenAI API key is missing.".```
3. Don't forget to create the '.env' file.
---



## ❓ Troubleshooting

### **1. "Error: OpenAI API key is missing."**
- Make sure `.env` file exists and contains `OPENAI_API_KEY`.
- Restart the backend after modifying `.env`.

### **2. "ConnectionError: Failed to establish a new connection"**
- Ensure `uvicorn` is running (`http://127.0.0.1:8000`).
- Restart backend (`uvicorn main:app --reload`).

### **3. "ValueError: could not convert string to float"**
- Your dataset might contain non-numeric values.
- Check for categorical data and encode it.

### **4. "openai.error.RateLimitError: You exceeded your current quota."**
- Check [OpenAI's Usage Page](https://platform.openai.com/account/usage).
- Upgrade your plan if needed.

---

## 🌟 Future Improvements
- Add **data visualization support** 📈.
- Integrate **AutoML for model selection** 🤖.
- Allow **user-configurable AI prompts** 💡.

---
