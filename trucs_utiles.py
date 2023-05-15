import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit.source_util import get_pages
import time

def boutons_rs(page_précédente : str, page_suivante : str):
    cr, cs = st.columns(2)
    st.markdown(
        """
        <style>
            div[data-testid="column"]:nth-of-type(1)
            {
                text-align: center;
            } 
            div[data-testid="column"]:nth-of-type(2)
            {
                text-align: center;
            } 
            div[id^="bui-"] > button:nth-child(1) > button:hover {
                background-color: #3DCDBC;
                color:#FAFAFA;
            }
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap');
            html, body, [class*="css"] 
            {			
			    font-family: 'Poppins', sans-serif;
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

def mise_en_forme_Question(question : str):
    st.markdown(
        f"""
            <h1>
                <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap">
                <style>
                    body {{
                        font-family: 'Poppins', sans-serif;
                    }}
                </style>
                <body>
                    {question}
                </body>
            </h1>
            """,
        unsafe_allow_html=True
    )

normal = """<style>
			    @import url('https://fonts.googleapis.com/css2?family=Poppins&display=swap');
			    html, body, [class*="css"]  {			
			        font-family: 'Poppins', sans-serif;
			    }
			</style>
			"""
