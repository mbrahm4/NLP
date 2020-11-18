import streamlit as st
import pandas as pd
import numpy as np
import time
import operator

st.title("PONDER")
st.header("Powerful quotes to motivate you")


# Import Data
def get_data():
    data = pd.read_json("quotes.json")
    return data

data = get_data()

# Take User Input
user_input = st.text_input("How are you feeling?")
run = st.button("Ponder")


# placeholder for sentiment between user input and quotes
def jaccard_similarity(query, document):
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    return len(intersection)/len(union)

quote_scored = {}

for quote in data['Quote']:
    score = jaccard_similarity(user_input, quote)
    quote_scored[quote] = score

quote = max(quote_scored.items(), key=operator.itemgetter(1))[0]
author = data[data['Quote']==quote]['Author'].unique()[0]

# Output quote

my_bar = st.progress(0)

if run:
    
    for percent_complete in range(100):
        
        time.sleep(0.0005)
        my_bar.progress(percent_complete + 1)
        
    st.write(quote)
    st.subheader(" - " + author)
    st.balloons()
