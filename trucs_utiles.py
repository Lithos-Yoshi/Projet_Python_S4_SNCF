import streamlit as st
from streamlit.delta_generator import DeltaGenerator
from streamlit_extras.switch_page_button import switch_page
import time

def transition(transition_num : str):
    st.markdown(
         f"""
         <style>
            .stApp {{
                background-image: url({transition_num});
                background-attachment: fixed;
                background-size: cover
            }}
         </style>
        """,
        unsafe_allow_html=True
    )

def boutons_rs(page_précédente : str, page_suivante : str, question : DeltaGenerator, champ : DeltaGenerator, transition_num : str):
    cr, cs = st.columns(2)
    st.markdown(
        """
        <style>
            div[data-testid="column"]:nth-of-type(1)
            {
                text-align: right;
            } 
            div[data-testid="column"]:nth-of-type(2)
            {
                text-align: left;
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
        Gbouton_r.empty()
        question.empty()
        champ.empty()
        transition(transition_num)
        time.sleep(2.5)
        switch_page(page_suivante)
    if Bretour:
        Gbouton_r.empty()
        switch_page(page_précédente)

def mise_en_forme_Question(question : str):
    return st.markdown(
        f"""
            <h2>
                <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap">
                <style>
                    body {{
                        font-family: 'Poppins', sans-serif;
                    }}
                </style>
                <body>
                    {question}
                </body>
            </h2>
            """,
        unsafe_allow_html=True
    )
