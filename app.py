import streamlit as st
import s3fs
import os
import pandas as pd

# Create connection object.
# `anon=False` means not anonymous, i.e. it uses access keys to pull data.
fs = s3fs.S3FileSystem(anon=False)

# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def read_csv(filename):
    with fs.open(filename) as f:
        return pd.read_csv(f)

filepath = 'fsdgbizbucket1/easy-image/database/User.csv'
users = read_csv(filepath)
st.dataframe(users)
