"""A small Streamlit app that displays data."""

import pandas as pd
import streamlit as st

st.set_page_config("Streamlit Example")

# Streamlit renders components in the order they appear in code
st.title("Streamlit Example App")

with st.container():
    st.header("Sample Data")
    df = pd.util.testing.makeMixedDataFrame()
    st.dataframe(df)