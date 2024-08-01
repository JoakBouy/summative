import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
import pandas as pd
from pyngrok import ngrok

from visualization import analysis_visualizations
from preprocessing import data_preprocessing
from splitting import data_splitting
from training import model_building
from testing import model_testing

# Title
st.title("Machine Learning Model to test for Presence of Cardio Vascular Diseases")

# Define the functions and their names
functions = [
    ("Data Analysis", analysis_visualizations),
    ("Data Preprocessing", data_preprocessing),
    ("Data Splitting", data_splitting),
    ("Model Training", model_building),
    ("Model Testing", model_testing)
]

# Initialize session state for the index of the current function
if 'current_function_index' not in st.session_state:
    st.session_state.current_function_index = 0

# Sidebar for navigation
st.sidebar.title("Navigation")
for i, (name, _) in enumerate(functions):
    if st.sidebar.button(name):
        st.session_state.current_function_index = i
        st.rerun()

# Display the current function
current_function_index = st.session_state.current_function_index
current_function_name, current_function = functions[current_function_index]

st.header(current_function_name)
current_function()

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    if st.session_state.current_function_index > 0:
        if st.button('Previous'):
            st.session_state.current_function_index -= 1
            st.rerun()

with col2:
    if st.session_state.current_function_index < len(functions) - 1:
        if st.button('Next'):
            st.session_state.current_function_index += 1
            st.rerun()

# Set up ngrok tunnel (this will run only when the script is run directly, not when imported)
if __name__ == '__main__':
    port = 8501
    public_url = ngrok.connect(port)
    print(f" * ngrok tunnel \"{public_url}\" -> \"http://127.0.0.1:{port}\"")