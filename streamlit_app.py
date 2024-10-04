# Import python packages
import streamlit as st
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie! :cup_with_straw:")
st.write(
    "Choose the fruits you want in your custom Smoothie!"
)

name_on_order = st.text_input("Name of Smoothie:")
st.write("The name of your Smoothie will be:", name_on_order)
st.write("The name of your Smoothie will be:", name_on_order)
