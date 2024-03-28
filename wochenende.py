import streamlit as st
from pathlib import Path

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text(encoding='utf-8')

# Read in the markdown file
instructions = read_markdown_file("instructions.md")

# Display the instructions in the app
st.markdown(instructions, unsafe_allow_html=True)