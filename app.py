import streamlit as st
import spacy

# Load model only once
@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

st.set_page_config(page_title="NER App", layout="centered")

st.title("🔍 Named Entity Recognition (NER)")
st.write("Enter a sentence and extract named entities.")

text = st.text_area("Enter text:")

if st.button("Extract Entities"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        doc = nlp(text)
        if doc.ents:
            for ent in doc.ents:
                st.write(f"**{ent.text}** → {ent.label_}")
        else:
            st.info("No entities found.")
