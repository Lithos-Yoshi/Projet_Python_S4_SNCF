# Imports
from trucs_utiles import *
import Main
# Mises en forme diverses
st.set_page_config(layout="wide")
st.markdown(
         f"""
         <style>
            .stApp {{
                background-color: #3DCDBC;
                background-attachment: fixed;
                background-size: cover
            }}
            div.stButton > button:hover {{
                background-color: #DBA574;
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
    question = "2. Quelle est la note moyenne attribuée par les Français(es) vis-à-vis de ponctualité de la SNCF en 2022 ? (/10)"
    # Appel d'une fonction générale de mise en forme de texte (ici de la question)
    zoneQuestion = mise_en_forme_Question(question)
    zoneText_input = st.empty()
    # On stocke la réponse au text_imput dans la variable globales définie dans Main.py
    Main.r2 = zoneText_input.text_input('Votre estimation (n\'oubliez d\'appuyer sur la touche "Entrée" avant de passer à la suite 😉) :')
    # Appel d'une fonction générale d'ajout de bontons "suivant" et "retour", avec leur comportement
    boutons_rs("question1", "réponse1", zoneQuestion, zoneText_input, "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjgyNjRjZmE4ZGExYzlkMTZiZTM0NzMxNDAwMTM4MjliOTgzNTZiMSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/kDAX9gEXsKJbCWBNnj/giphy.gif")