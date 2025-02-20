import spacy

# Load a pre-trained spaCy model for NLP
nlp = spacy.load("en_core_web_sm")

def interpret_query(query):
    doc = nlp(query)
    for ent in doc.ents:
        if "regression" in query:
            return "perform_regression_analysis"
        elif "visualization" in query:
            return "generate_visualization"
    return "unknown_query"
