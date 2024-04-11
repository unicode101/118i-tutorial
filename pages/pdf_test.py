import streamlit as st
import fitz  # PyMuPDF

# Create a file uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Load the PDF
    pdf = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    
    # Analyze the PDF
    for i in range(len(pdf)):
        page = pdf.load_page(i)
        text = page.get_text("text")
        st.write(f"Content of Page {i+1}:")
        st.write(text)