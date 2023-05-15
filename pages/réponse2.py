# IMPORTS --------------------------------------------------------------------------------------------------------------
import pandas as pd
import streamlit
from streamlit_extras.chart_container import chart_container
import Main
from trucs_utiles import *

# On définit quelques variables pour nous simplifier la vie !
fichier1417 = "2014-2017 barometre-notes-dopinion-sncf.csv"
fichier1821 = "2018-2021 barometre-notes-dopinion-sncf-gmv.csv"
fichier2223 = "2022-2023 sncf-image-open-data-mensuel-harris.csv"

# Définition d'une fonction de chargement des données (en particulier, elle charge nb_lignes lignes de données)
@st.cache_data
def chargement_brut(données : str, nb_lignes):
    données_brutes = pd.read_csv(données, delimiter=";", nrows=nb_lignes)
    données_brutes["Date"] = pd.to_datetime(données_brutes["Date"])
    return données_brutes
# On charge 10000 lignes de données de différents datasets
satis1417 = chargement_brut(fichier1417, 10000)
satis1821 = chargement_brut(fichier1821, 10000)
satis2223 = chargement_brut(fichier2223, 10000)
satis1417["Date"] = satis1417["Date"].dt.year
moyenne = satis1417.groupby(["Date", "Notes d'opinion"]).mean().reset_index()
moyenne.drop(moyenne.columns[[2]], axis=1, inplace=True)
st.write(moyenne)
st.line_chart(moyenne, x="Date", y=["innovation", "ponctualité", "globale", "prix"])