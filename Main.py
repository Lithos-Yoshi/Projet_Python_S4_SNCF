# Main.py correspond à la page d'accueil du projet. Le nom du fichier est en majuscule selon la documentation de
# streamlit.io relative aux applications multipages.


# LIBRAIRIES -----------------------------------------------------------------------------------------------------------
import streamlit as st
# Importation d'éléments de streamlit-extras, une librairie implémentant des fonctionnalités non présentes dans la
# librairie streamlit de base, comme par exemple la possibilité de changer de page à l'aide d'un bouton de façon simple.
from streamlit_extras.switch_page_button import switch_page
import time

# Variables globales ---------------------------------------------------------------------------------------------------
r1 : str
r2 : str
r3 : str
r4 : str


# PERSONNALISATION -----------------------------------------------------------------------------------------------------
# Police personnalisée (non disponible par défaut)
police = """<style>
			    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap');
			    html, body, [class*="css"]  {			
			        font-family: 'Poppins', sans-serif;
			    }
			</style>"""
st.markdown(police, unsafe_allow_html=True)

# FONCTIONS & MÉTHODES -------------------------------------------------------------------------------------------------
# Définition d'une fonction de transition pour passer de la page d'accueil à la première page de questions
def transition():
    # On vient forcer le fond (background) à charger un gif que j'ai créé et stocké sur
    # giphy.com quand cette fonction est appelée.
    # NB : sans connexion Internet, le gif ne pourra être chargé. Néanmoins, puisqu'il
    # est trop complexe de le forcer à prendre un fichier local et que le projet doit
    # de toutes façons tourner avec Internet, j'ai décidé de conserver cette solution.
    st.markdown(
         f"""<style>
         .stApp {{
             background-image: url("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTJlZTNlZTNlMTM5NjFiZGNjZjU3NDg5ZDU2MjNkYTlkMDE5NjkyYiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/J04NvbFLjPX4GGipB4/giphy.gif");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>""",
         unsafe_allow_html=True
     )

#
# Ce qui suit est un "trick" qui permet de visuellement centrer des éléments sur l'écran puisque que ce n'est pas
# possible de le faire de façon native. On divise l'écran en trois colonnes et on vient mettre ce qui nous intéresse
# dans la colonne centrale.
Cvide1, Ctitre, Cvide3 = st.columns(3)
with Ctitre:
    Mtitre = st.markdown("<h1 style='text-align: center'>Quiz SNCF</h1>", unsafe_allow_html=True)
    Gbouton = st.empty()
    Bcommencer = Gbouton.button("Commencer")

# On vient gérer l'événement du clic sur le bouton. Une fois cliqué, les conteneurs streamlit sont vidés pour laisser
# une page "vierge" avec uniquement le fond. Ce dernier est donc une transition animée en gif. Pour gérer la latence
# variable de chargement, je laisse un peu plus de temps que la durée de l'animation pour passer à la page suivante.
if Bcommencer:
    Mtitre.empty()
    Gbouton.empty()
    transition()
    time.sleep(5)
    switch_page("question1")