import streamlit as st
import spacy

@st.cache_resource
def load_model():
    return spacy.load("en_core_web_sm")

nlp = load_model()

st.title("NER App")

text = st.text_input("Enter text")

if text:
    doc = nlp(text)
    for ent in doc.ents:
        st.write(ent.text, ent.label_)

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


