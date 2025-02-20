import openai

def generate_report(analysis_results):
    prompt = f"Generate a detailed report based on the following analysis: {analysis_results}"
    response = openai.Completion.create(
        engine="text-davinci-003",  # Replace with the appropriate model
        prompt=prompt,
        max_tokens=500
    )
    report = response.choices[0].text.strip()
    return report
