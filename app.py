import streamlit as st
import spacy

st.set_page_config(page_title="NER App", layout="centered")

@st.cache_resource
def load_model():
    try:
        return spacy.load("en_core_web_sm")
    except:
        return spacy.blank("en")

nlp = load_model()

st.title("Named Entity Recognition (NER)")
st.write("Enter text to extract named entities.")

text = st.text_area("Enter text:", "Virat Kohli was born in Delhi")

if st.button("Analyze"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        doc = nlp(text)
        if doc.ents:
            for ent in doc.ents:
                st.write(f"**{ent.text}** → {ent.label_}")
        else:
            st.info("No entities found (model may be blank).")
