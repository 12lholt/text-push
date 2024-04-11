import streamlit as st
from azure.storage.blob import BlobClient
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Retrieve environment variables
STORAGE_URL = os.getenv('STORAGE_URL')
SAS_TOKEN = os.getenv('SAS_TOKEN')
CONTAINER_NAME = os.getenv('CONTAINER_NAME')
BLOB_NAME = os.getenv('BLOB_NAME')

def upload_string_to_blob(upload_string):
    """
    Uploads a string to Azure Blob Storage.
    """
    blob_url = f"{STORAGE_URL}{CONTAINER_NAME}/{BLOB_NAME}{SAS_TOKEN}"
    blob_client = BlobClient.from_blob_url(blob_url)
    blob_client.upload_blob(upload_string, overwrite=True)

# Streamlit UI
st.title('Azure Blob Text Uploader')

# Text box for input
user_input = st.text_area("Insert text to upload to Azure Blob Storage:", height=300, key='text_box')

# Center the submit button
col1, col2, col3 = st.columns([1,1,1])
with col2:
    submit = st.button('Submit')

if submit:
    upload_string_to_blob(user_input)
    st.success("Text uploaded successfully!")
