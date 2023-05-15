# IMPORTS --------------------------------------------------------------------------------------------------------------
import pandas as pd
import streamlit
import streamlit_extras
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


col1, col2 = st.columns(2)
with col1:
    titre = "2. Données : Satisfaction des Français(es) quant à la ponctualité de la SNCF"
    mise_en_forme_Question(titre)
    st.markdown(
        f"""
                <h5>
                    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Poppins&display=swap">
                    <style>
                        body {{
                            font-family: 'Poppins', sans-serif;
                            font-size: 16;
                        }}
                    </style>
                    <body>
                        Selon toi, les Français(es) ont attribué la note de {Main.r2}/10 concernant la ponctualité de la SNCF en 2022. Regarde si tu as vu juste ! 👇
                    </body>
                </h5>
                """,
        unsafe_allow_html=True
    )
    st.text("")
    st.markdown(
        """
        <div style = "text-align: center">
            Évolution de la satisfaction des Français(es) quant à la ponctualité de la SNCF (/10) (ressources.data.sncf.com)
        </div>
        """,
        unsafe_allow_html=True
    )
    # Ce qui suit n'est pas très propre et un peu long mais cela a le mérite de fonctionner...
    satis1417["Date"] = satis1417["Date"].dt.year
    moyenne1417 = satis1417.groupby(["Date", "Notes d'opinion"]).mean().reset_index()
    moyenne1417.drop(moyenne1417.columns[[2]], axis=1, inplace=True)
    ponctualité1417 = moyenne1417.loc[moyenne1417["Notes d'opinion"] == "ponctualité"]

    satis1821["Date"] = satis1821["Date"].dt.year
    moyenne1821 = satis1821.groupby(["Date", "Indicateurs"]).mean().reset_index()
    moyenne1821.drop(moyenne1821.columns[[3, 4]], axis=1, inplace=True)
    ponctualité1821 = moyenne1821.loc[moyenne1821["Indicateurs"] == "Ponctualité"]

    satis2223["Date"] = satis2223["Date"].dt.year
    moyenne2223 = satis2223.groupby(["Date", "Indicateurs"]).mean().reset_index()
    moyenne2223.drop(moyenne2223.columns[[3, 4]], axis=1, inplace=True)
    ponctualité2223 = moyenne2223.loc[moyenne2223["Indicateurs"] == "Ponctualité"]

    ponctualité1417 = ponctualité1417.rename(columns={"Réputation": "Global"})
    ponctualité1821 = ponctualité1821.rename(columns={"Français": "Global"})
    total1421 = pd.concat([ponctualité1417, ponctualité1821]).reset_index()
    total1421.drop(total1421.columns[[0, 2, 4]], axis=1, inplace=True)

    # On divise par 10 car on a des % (donc des résultats sur 100) inexploitables. Cette opération est discutable.
    ponctualité2223["Global"] = ponctualité2223["Global"] / 10
    total1423 = pd.concat([total1421, ponctualité2223]).reset_index()
    total1423.drop(total1423.columns[[0, 3]], axis=1, inplace=True)
    with chart_container(total1423, ("Graphique", "Tableau", "Tout masquer"), ""):
        st.line_chart(total1423, x="Date", y="Global")

