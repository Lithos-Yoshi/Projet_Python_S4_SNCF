import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
from trucs_utiles import *
import Main

st.title("2. Selon vous, suite de la question un peu longue ?")
st.text_input("Votre réponse ?" + Main.r1)
boutons_rs("question1", "question3")


