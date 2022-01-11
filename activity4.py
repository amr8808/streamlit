import streamlit as st
import pandas as pd

st.write('# This is my n00b streamlit app')

st.write('### Everyone says RUST is better than python, but is it?')

df = pd.DataFrame({'Name': ['Arjan'], 'Thoughts': ['No'], 'is n00b': ['No']})
df.set_index('Name', inplace=True)
st.write("Initializing n00b list")
st.write(df)



myname = st.text_input('What is your name?')

input_value = st.text_input("Is RUST better than python?")

# @st.cache(allow_output_mutation=True)
# def setup():
#     print("Initializing n00b list")
# return st.write(df)


# list = setup()

if st.button("Submit response"):
    st.write(input_value.capitalize()+'?  \n# Seriously????  \n## .... n00b....')

