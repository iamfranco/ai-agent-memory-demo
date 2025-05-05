import streamlit as st
from db.vector_db import VectorDB
from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import DocumentStream
from io import BytesIO

import torch
torch.classes.__path__ = [] # add this line to manually set it to empty. 

def _get_and_show_vector_db_collections():
  collections = st.session_state.vector_db.get_collections()
  st.write(collections)

def _create_vector_db_collection_section():
  with st.form("collection creation form"):
    st.subheader("Create a new collection")
    
    collection_name = st.text_input("Collection name")
    vector_size = st.number_input("Vector size", min_value=1, max_value=1536, value=1536)
    submitted = st.form_submit_button("Create Collection")

    if submitted:
      if not collection_name:
        st.error("Please enter a collection name.")
        return

      success = st.session_state.vector_db.create_collection(collection_name, vector_size)
      if success:
        st.success("Collection created successfully!")
      else:
        st.error("Failed to create collection. Please check if collection name is valid.")

def _pdf_selection_section():
  with st.form("pdf selection form"):
    st.subheader("Select a PDF file to interpret")
    
    pdf_file = st.file_uploader("Select PDF to interpret", type=["pdf"])
    submitted = st.form_submit_button("Interpret PDF")
    
    if submitted and pdf_file:
      with st.spinner("Interpreting PDF...", show_time=True):
        pdf_bytes = pdf_file.read()
        buf = BytesIO(pdf_bytes)
        source = DocumentStream(name=pdf_file.name, stream=buf)

        converter = DocumentConverter()
        result = converter.convert(source)
        result_md = result.document.export_to_markdown()

        with st.expander("PDF Interpretation Result", expanded=True):
          st.markdown(result_md)

def vector_db_page():
  if "vector_db" not in st.session_state:
    st.session_state.vector_db = VectorDB()

  st.button("Get VectorDB Collections", on_click=_get_and_show_vector_db_collections)

  _create_vector_db_collection_section()

  _pdf_selection_section()