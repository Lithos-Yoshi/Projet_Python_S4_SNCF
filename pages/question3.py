# Imports
from trucs_utiles import *
import Main
# Mise en forme du fond
st.markdown(
         f"""
         <style>
            .stApp {{
                background-color: #DBA574;
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
    question = "3. Selon vous, suite de la question un peu longue ?"
    # Appel d'une fonction générale de mise en forme de texte (ici de la question)
    zoneQuestion = mise_en_forme_Question(question)
    zoneText_input = st.empty()
    # On stocke la réponse au text_imput dans la variable globales définie dans Main.py
    Main.r3 = zoneText_input.text_input("Votre réponse ?")
    # Appel d'une fonction générale d'ajout de bontons "suivant" et "retour", avec leur comportement
    boutons_rs("question2", "réponse1", zoneQuestion, zoneText_input, "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWI1MzEyODlhODViMGNjZjE0ZDE0NWYzZTY5MGU4YzhjOTRkMGJjOSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/hq8MAOMhX3iIYjqcSk/giphy.gif")