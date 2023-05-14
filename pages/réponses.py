import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
DATE_COLUMN = "regularite-mensuelle-ter.csv"
FICHIER_DONNÉES = "regularite-mensuelle-ter.csv"

@st.cache_data
def load_data(nb_lignes):
    data = pd.read_csv(FICHIER_DONNÉES, delimiter=";", nrows=nb_lignes)
    return data