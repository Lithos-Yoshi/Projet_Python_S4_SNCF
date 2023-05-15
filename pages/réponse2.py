# IMPORTS --------------------------------------------------------------------------------------------------------------
import numpy as np
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

st.set_page_config(layout="wide")

# Définition d'une fonction de chargement des données (en particulier, elle charge nb_lignes lignes de données)
@st.cache_data
def chargement_brut(données : str, nb_lignes):
    données_brutes = pd.read_csv(données, delimiter=";", nrows=nb_lignes)
    données_brutes["Date"] = pd.to_datetime(données_brutes["Date"])
    return données_brutes
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
    # Bidouillages Ponctualité
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
    total1423 = total1423.rename(columns={"Global": "Ponctualité"})
    with chart_container(total1423, ("Graphique", "Tableau", "Tout masquer"), ""):
        st.line_chart(total1423, x="Date", y="Ponctualité")

with col2:
    # Bidouillages Opinion globale
    # Ce qui suit n'est pas très propre et un peu long mais cela a le mérite de fonctionner...
    opinionglobale1417 = moyenne1417.loc[moyenne1417["Notes d'opinion"] == "globale"]
    opinionglobale1821 = moyenne1821.loc[moyenne1821["Indicateurs"] == "Note globale"]
    opinionglobale2223 = moyenne2223.loc[moyenne2223["Indicateurs"] == "Opinion globale"]
    opinionglobale1417 = opinionglobale1417.rename(columns={"Réputation": "Global"})
    opinionglobale1821 = opinionglobale1821.rename(columns={"Français": "Global"})
    totalop1421 = pd.concat([opinionglobale1417, opinionglobale1821]).reset_index()
    totalop1421.drop(totalop1421.columns[[0, 2, 4]], axis=1, inplace=True)
    # On divise par 10 car on a des % (donc des résultats sur 100) inexploitables. Cette opération est discutable.
    opinionglobale2223["Global"] = opinionglobale2223["Global"] / 10
    totalop1423 = pd.concat([totalop1421, opinionglobale2223]).reset_index()
    totalop1423.drop(totalop1423.columns[[0, 3]], axis=1, inplace=True)
    totalop1423 = totalop1423.rename(columns={"Global": "Opinion globale"})

    # Bidouillages Environnement
    moyenne1417["Environnement"] = np.NaN
    environnement1821 = moyenne1821.loc[moyenne1821["Indicateurs"] == "Environnement"]
    environnement2223 = moyenne2223.loc[moyenne2223["Indicateurs"] == "Environnement"]
    environnement1821 = environnement1821.rename(columns={"Français": "Global"})
    environnement2223["Global"] = environnement2223["Global"] / 10
    totalenv1823 = pd.concat([environnement1821, environnement2223]).reset_index()
    totalenv1823.drop(totalenv1823.columns[[0, 2]], axis=1, inplace=True)
    totalenv1823 = totalenv1823.rename(columns={"Global": "Environnement"})

    # Bidouillages Information voyageurs
    moyenne1417["Information voyageurs"] = np.NaN
    infovoyageurs1821 = moyenne1821.loc[moyenne1821["Indicateurs"] == "Information Voyageurs"]
    infovoyageurs2223 = moyenne2223.loc[moyenne2223["Indicateurs"] == "Information voyageurs"]
    infovoyageurs1821 = infovoyageurs1821.rename(columns={"Français": "Global"})
    infovoyageurs2223["Global"] = infovoyageurs2223["Global"] / 10
    totalinfo1823 = pd.concat([infovoyageurs1821, infovoyageurs2223]).reset_index()
    totalinfo1823.drop(totalinfo1823.columns[[0, 2]], axis=1, inplace=True)
    totalinfo1823 = totalinfo1823.rename(columns={"Global": "Information voyageurs"})

    # Bidouillages Innovation
    # Ce qui suit n'est pas très propre et un peu long mais cela a le mérite de fonctionner...
    innovation1417 = moyenne1417.loc[moyenne1417["Notes d'opinion"] == "innovation"]
    innovation1821 = moyenne1821.loc[moyenne1821["Indicateurs"] == "Innovation"]
    innovation2223 = moyenne2223.loc[moyenne2223["Indicateurs"] == "Innovation"]
    innovation1417 = innovation1417.rename(columns={"Réputation": "Global"})
    innovation1821 = innovation1821.rename(columns={"Français": "Global"})
    totalinnov1421 = pd.concat([innovation1417, innovation1821]).reset_index()
    totalinnov1421.drop(totalinnov1421.columns[[0, 2, 4]], axis=1, inplace=True)
    # On divise par 10 car on a des % (donc des résultats sur 100) inexploitables. Cette opération est discutable.
    innovation2223["Global"] = innovation2223["Global"] / 10
    totalinnov1423 = pd.concat([totalinnov1421, innovation2223]).reset_index()
    totalinnov1423.drop(totalinnov1423.columns[[0, 3,4]], axis=1, inplace=True)
    totalinnov1423 = totalinnov1423.rename(columns={"Global": "Innovation"})

    # Bidouillages Prix
    # Ce qui suit n'est pas très propre et un peu long mais cela a le mérite de fonctionner...
    prix1417 = moyenne1417.loc[moyenne1417["Notes d'opinion"] == "prix"]
    prix1821 = moyenne1821.loc[moyenne1821["Indicateurs"] == "Prix"]
    prix2223 = moyenne2223.loc[moyenne2223["Indicateurs"] == "Prix"]
    prix1417 = prix1417.rename(columns={"Réputation": "Global"})
    prix1821 = prix1821.rename(columns={"Français": "Global"})
    totalprix1421 = pd.concat([prix1417, prix1821]).reset_index()
    totalprix1421.drop(totalprix1421.columns[[0, 2, 4]], axis=1, inplace=True)
    # On divise par 10 car on a des % (donc des résultats sur 100) inexploitables. Cette opération est discutable.
    prix2223["Global"] = prix2223["Global"] / 10
    totalprix1423 = pd.concat([totalprix1421, prix2223]).reset_index()
    totalprix1423.drop(totalprix1423.columns[[0, 3, 4]], axis=1, inplace=True)
    totalprix1423 = totalprix1423.rename(columns={"Global": "Prix"})

    tableautotal = pd.merge(
        pd.merge(
            pd.merge(
                pd.merge(
                    pd.merge(
                        totalop1423, total1423, on="Date"
                    ),
                    totalenv1823, on="Date", how="outer"
                ),
                totalinfo1823, on="Date", how="outer"
            ),
            totalinnov1423, on="Date", how="outer"
        ),
        totalprix1423, on="Date", how="outer"
    )
    st.markdown(
        """
        <style>
            div[data-testid="column"]:nth-of-type(2)
            {
                text-align: right;
            } 
            </style>""",
        unsafe_allow_html=True
    )
    Gbouton_r = st.empty()
    Bretour = Gbouton_r.button("⬅️ Retour")
    if Bretour:
        switch_page("réponse1")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.markdown(
        """
        <div style = "text-align: center">
            Évolution de la satisfaction des Français(es) sur différents critères (/10) (ressources.data.sncf.com)
        </div>
        """,
        unsafe_allow_html=True
    )
    # Affichage graphique complet
    with chart_container(tableautotal, ("Graphique", "Tableau", "Tout masquer"), ""):
        st.line_chart(tableautotal, x="Date", y=["Opinion globale", "Prix", "Innovation", "Information voyageurs", "Environnement", "Ponctualité"])

st.write("NB : les données entre 2022 et 2023 étaient exprimées en %. Elles ont été divisées par 10 pour coller aux autres données.")