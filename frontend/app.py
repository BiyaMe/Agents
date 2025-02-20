import streamlit as st
import pandas as pd
import io
import requests
import sys

# from backend.data_analysis import auto_data_analysis
# from backend.feedback import store_feedback
# from backend.nlp_processing import interpret_query
# from backend.llm_integration import generate_report

# Streamlit app title
st.title("Data Science Assistant")

# File upload section
uploaded_file = st.file_uploader("Upload your dataset (CSV)", type=["csv"])

if uploaded_file:
    # Read the uploaded file into a DataFrame
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview")
    st.dataframe(df.head())

    # Send file to backend server (running on http://localhost:8000)
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)
    files = {"file": buffer.getvalue()}

    response = requests.post("http://localhost:8000/upload/", files=files)

    if response.status_code == 200:
        result = response.json()

        # Display results of the backend analysis
        st.write("### Exploratory Data Analysis")
        st.json(result["eda"])

        st.write("### AI-Generated Data Insights")
        st.write(result["insights"])  # Display AI-generated insights from LLM

        st.write("### Suggested Machine Learning Model")
        st.json(result["model"])
    else:
        print("Error:Unable to connect to the backend,", response.status_code)

    # Additional analysis on the uploaded data (using auto_data_analysis)
    # if st.button("Run Automated Analysis"):
    #     model, mse = auto_data_analysis(df)
    #     st.write(f"Model: {model}")
    #     st.write(f"Mean Squared Error: {mse}")

    #     # Generate a report from the model analysis (using LLM integration)
    #     report = generate_report(mse)
    #     st.write("### Generated Report")
    #     st.write(report)

    # # Collect feedback from the user
    # feedback = st.text_input("Provide feedback on the analysis")
    # if feedback:
    #     store_feedback(feedback, model)
