import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv("happy.csv")

happiness = df['happiness']
gdp = df['gdp']
generosity = df['generosity']

st.title("In Search for Happiness")

opt1 = st.selectbox("Select the data for X-axis", ("Happiness", "GDP", "Generosity"))
opt2 = st.selectbox("Select the data for Y-axis", ("Happiness", "GDP", "Generosity"))

data_mapping = {
    "Happiness": df["happiness"],
    "GDP": df["gdp"],
    "Generosity": df["generosity"]
}

optx = data_mapping[opt1]
opty = data_mapping[opt2]

st.subheader(f"{opt1} and {opt2}")

figure = px.scatter(x=optx, y=opty, labels={"x": f"{opt1}", "y": f"{opt2}"})
st.plotly_chart(figure)

