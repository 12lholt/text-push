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
AUDIO_BLOB_NAME = os.getenv('AUDIO_BLOB_NAME')

def upload_file_to_blob(blob_name, file_data):
    """
    Uploads a file to Azure Blob Storage.
    """
    blob_url = f"{STORAGE_URL}{CONTAINER_NAME}/{blob_name}{SAS_TOKEN}"
    blob_client = BlobClient.from_blob_url(blob_url)
    blob_client.upload_blob(file_data, overwrite=True)

# Streamlit UI
st.title('Azure Blob Uploader')

# Section for uploading text
st.header("Upload Text")
user_input = st.text_area("Insert text to upload to Azure Blob Storage:", height=150, key='text_box')
submit_text = st.button('Upload Text')

if submit_text:
    upload_file_to_blob(BLOB_NAME + '.txt', user_input.encode())
    st.success("Text uploaded successfully!")

# Section for uploading MP3 files
st.header("Upload MP3 File")
uploaded_file = st.file_uploader("Choose a MP3 file", type=['mp3'], key='file_uploader')
submit_file = st.button('Upload MP3')

if submit_file and uploaded_file is not None:
    upload_file_to_blob(AUDIO_BLOB_NAME + '.mp3', uploaded_file.getvalue())
    st.success("MP3 file uploaded successfully!")
