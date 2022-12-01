import streamlit as st
import s3fs
import os
import pandas as pd

# Create connection object.
# `anon=False` means not anonymous, i.e. it uses access keys to pull data.
fs = s3fs.S3FileSystem(anon=False, key=os.getenv('AWS_ACCESS_KEY_ID'), secret=os.getenv('AWS_SECRET_ACCESS_KEY'))
st.write(os.getenv('AWS_ACCESS_KEY_ID'))
st.write(os.getenv('AWS_SECRET_ACCESS_KEY'))

# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def read_csv(filename):
    df = pd.read_csv(filename)
    return df

filepath = 'fsdgbizbucket1/User.csv'
users = read_csv(filepath)
st.dataframe(users)
