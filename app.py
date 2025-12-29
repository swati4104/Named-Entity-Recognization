import streamlit as st
import re

st.set_page_config(page_title="Simple NER App")

st.title("🧠 Simple Named Entity Recognition")

text = st.text_area("Enter text")

if st.button("Extract Entities"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        # Simple rule-based NER
        words = text.split()
        entities = [word for word in words if word.istitle()]

        if entities:
            st.success("Entities found:")
            for e in entities:
                st.write("•", e)
        else:
            st.info("No entities found.")
