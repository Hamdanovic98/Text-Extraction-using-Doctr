import streamlit as st
from PIL import Image
from doctr.models import ocr_predictor
from doctr.io import DocumentFile
from pdf2image import convert_from_bytes
import pandas as pd
import io
import tempfile
from transformers import pipeline

def extract_text_from_document(document):
    model = ocr_predictor(pretrained=True)
    result = model(document)
    return result

st.title("Text Extraction with docTR")

uploaded_file = st.file_uploader("Choose a PDF or image file", type=["pdf", "png", "jpg", "jpeg"])

if uploaded_file is not None:
    with st.spinner('Extracting Text...'):
        if uploaded_file.type == "application/pdf":
            # Convert PDF to images
            images = convert_from_bytes(uploaded_file.getvalue())
            image = images[0]  # Use the first page/image
            with tempfile.NamedTemporaryFile(suffix=".png") as tmp_file:
                image_path = tmp_file.name
                image.save(image_path)
                document = DocumentFile.from_images([image_path])
        else:
            image = Image.open(io.BytesIO(uploaded_file.read()))
            with tempfile.NamedTemporaryFile(suffix=".png") as tmp_file:
                image_path = tmp_file.name
                image.save(image_path)
                document = DocumentFile.from_images([image_path])

    # Perform OCR and store the result in the 'result' variable
    result = extract_text_from_document(document)

    st.success('Extraction completed!')

    # Create a layout with two columns
    col1, col2 = st.columns([3, 1])

    # Display the uploaded document image in the first column
    with col1:
        st.subheader("Uploaded Document")
        st.image(image, caption='Uploaded Document', use_column_width=True)

    # Extract and display the text in the second column
    with col2:
        data = []
        for page in result.pages:
            for block in page.blocks:
                for line in block.lines:
                    for word in line.words:
                        data.append([word.value])

        df = pd.DataFrame(data, columns=['Text'])

        # Display the table with extracted text
        st.subheader("Extracted Text")
        st.table(df)

