# Imports
from trucs_utiles import *
import Main
# Mise en forme du fond
st.markdown(
         f"""
         <style>
            .stApp {{
                background-color: #39342E;
                background-attachment: fixed;
                background-size: cover
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
    Main.r1 = zoneText_input.text_input("Votre estimation :")
    # Appel d'une fonction générale d'ajout de bontons "suivant" et "retour", avec leur comportement
    boutons_rs("Main", "question2", zoneQuestion, zoneText_input, "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTgyMzkzMDA4YzRiZTE2YjZjNzgwZDdkZGFjZmU4YTQ0Y2IxZTdkZiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/S9LlBCXDfBHQZ34cHH/giphy.gif")