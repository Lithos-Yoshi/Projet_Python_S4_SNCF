import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import time
from trucs_utiles import *
import Main

st.title("1. Quelle est la proportion moyenne trains en retard/trains programmés en 2022 (en %) ?")
Main.r1 = st.text_input("Votre estimation :")
boutons_rs("Main", "question2")


