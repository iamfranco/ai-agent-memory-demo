import streamlit as st
from db.vector_db import VectorDB

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


def vector_db_page():
  if "vector_db" not in st.session_state:
    st.session_state.vector_db = VectorDB()

  st.button("Get VectorDB Collections", on_click=_get_and_show_vector_db_collections)

  _create_vector_db_collection_section()