import streamlit as st
import spacy

# Load spaCy model
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

# App UI
st.title("Named Entity Recognition (NER) App")
st.write("Enter a sentence to extract named entities like PERSON, GPE, ORG, etc.")

# Text input
text = st.text_area("Enter text:", "Virat Kohli was born in Delhi")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        doc = nlp(text)

        st.subheader("Extracted Entities")
        if doc.ents:
            for ent in doc.ents:
                st.write(f"**{ent.text}** → {ent.label_}")
        else:
            st.write("No entities found.")
