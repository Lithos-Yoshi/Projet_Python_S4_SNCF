# Imports
from trucs_utiles import *
import Main
# Mises en forme diverses
st.set_page_config(layout="wide")
st.markdown(
         f"""
         <style>
            .stApp {{
                background-color: #39342E;
                background-attachment: fixed;
                background-size: cover
            }}
            div.stButton > button:hover {{
                background-color: #3DCDBC;
                color:#FAFAFA;
            }}
            @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap');
		    html, body, [class*="css"]  {{			
			    font-family: 'Poppins', sans-serif;
		    }}
        </style>
        """,
        unsafe_allow_html=True
    )
# Mise en place des colonnes pour centrer le contenu
c1, c2, c3 = st.columns(3)
with c2:
    question = "1. Quelle est le rapport moyen TER en retard / TER programmés en 2022 (en %) ?"
    # Appel d'une fonction générale de mise en forme de texte (ici de la question)
    zoneQuestion = mise_en_forme_Question(question)
    zoneText_input = st.empty()
    # On stocke la réponse au text_imput dans la variable globales définie dans Main.py
    Main.r1 = zoneText_input.text_input('Votre estimation (n\'oubliez d\'appuyer sur la touche "Entrée" avant de passer à la suite 😉) :')
    # Appel d'une fonction générale d'ajout de bontons "suivant" et "retour", avec leur comportement
    boutons_rs("Main", "question2", zoneQuestion, zoneText_input, "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTgyMzkzMDA4YzRiZTE2YjZjNzgwZDdkZGFjZmU4YTQ0Y2IxZTdkZiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/S9LlBCXDfBHQZ34cHH/giphy.gif")