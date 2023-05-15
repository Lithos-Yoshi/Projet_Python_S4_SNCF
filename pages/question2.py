import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
from trucs_utiles import *
import Main

question = "2. Selon vous, suite de la question un peu longue ?"
mise_en_forme_Question(question)
st.text_input("Votre réponse ?")
boutons_rs("question1", "question3")


