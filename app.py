import streamlit as st
import spacy

st.set_page_config(page_title="NER App", layout="centered")

# Load model safely (only once)
@st.cache_resource
def load_nlp():
    return spacy.load("en_core_web_sm")

nlp = load_nlp()

st.title("🔍 Named Entity Recognition (spaCy)")

text = st.text_area("Enter text:")

if st.button("Extract Entities"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        doc = nlp(text)

        if doc.ents:
            for ent in doc.ents:
                st.write(f"**{ent.text}** → {ent.label_}")
        else:
            st.info("No entities found.")
