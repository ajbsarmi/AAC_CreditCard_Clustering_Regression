import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Home")
st.write("Hello World")

# Create data frame
df = pd.read_csv("../DSFC13_Sprint1/Data/cc_clean.csv")
st.write(df.head())
