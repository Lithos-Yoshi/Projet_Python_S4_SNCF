import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import time

def transition():
    st.markdown(
         f"""<style>
         .stApp {{
             background-image: url("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTJlZTNlZTNlMTM5NjFiZGNjZjU3NDg5ZDU2MjNkYTlkMDE5NjkyYiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/J04NvbFLjPX4GGipB4/giphy.gif");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>""",
         unsafe_allow_html=True
     )
    
Cvide1, Ctitre, Cvide3 = st.columns(3)
with Cvide1:
    st.text('')
with Ctitre:
    Mtitre = st.markdown("<h1 style='text-align: center'>Quiz SNCF</h1>", unsafe_allow_html=True)
    Gbouton = st.empty()
    Bcommencer = Gbouton.button("Commencer")
with Cvide3:
    st.text('')

if Bcommencer:
    Mtitre.empty()
    Gbouton.empty()
    transition()
    time.sleep(5)
    switch_page("questions")

DATE_COLUMN = "regularite-mensuelle-ter.csv"
FICHIER_DONNÉES = "regularite-mensuelle-ter.csv"

@st.cache_data
def load_data(nb_lignes):
    data = pd.read_csv(FICHIER_DONNÉES, delimiter=";", nrows=nb_lignes)
    return data

police = """<style>
			    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap');
			    html, body, [class*="css"]  {			
			        font-family: 'Poppins', sans-serif;
			    }
			</style>"""
st.markdown(police, unsafe_allow_html=True)
