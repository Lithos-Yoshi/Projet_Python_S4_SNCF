import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit.source_util import get_pages
import time

def boutons_rs(page_précédente : str, page_suivante : str):
    cr, cs = st.columns(2)
    st.markdown(
        """<style>
            div[data-testid="column"]:nth-of-type(1)
            {
                text-align: center;
            } 
            div[data-testid="column"]:nth-of-type(2)
            {
                text-align: center;
            } 
        </style>""",
        unsafe_allow_html=True
    )

    with cs:
        Gbouton_s = st.empty()
        Bsuivant = Gbouton_s.button("Suivant")
    with cr:
        Gbouton_r = st.empty()
        Bretour = Gbouton_r.button("Retour")
    if Bsuivant:
        Gbouton_s.empty()
        switch_page(page_suivante)
    if Bretour:
        Gbouton_r.empty()
        switch_page(page_précédente)