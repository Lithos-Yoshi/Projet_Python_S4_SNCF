# IMPORTS --------------------------------------------------------------------------------------------------------------
import pandas as pd
import streamlit
import streamlit_extras
from streamlit_extras.chart_container import chart_container
import Main
from trucs_utiles import *

# On définit quelques variables pour nous simplifier la vie !
date = "Date"
fichier = "regularite-mensuelle-ter.csv"
nbretard = "Nombre de trains en retard en définitive"
retard = "Retards"
nbprog = "Nombre de trains programmés"
prog = "Trains programmés"
prog12 = "Trains programmés /12"
retardprog = "Retard/programmés (%)"
retardprog100 = "Retard/programmés x100 (%)"

# Mises en forme diverses
st.markdown(
         f"""
         <style>
            .stApp {{
                background-color: #DBA574;
                background-attachment: fixed;
                background-size: cover
            }}            
            div.stButton > button:hover {{
                background-color: #39342E;
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

# Définition d'une fonction de chargement des données (en particulier, elle charge nb_lignes lignes de données)
@st.cache_data
def chargement_brut(nb_lignes):
    données_brutes = pd.read_csv(fichier, delimiter=";", nrows=nb_lignes)
    données_brutes["Date"] = pd.to_datetime(données_brutes["Date"])
    return données_brutes
# On charge 10000 lignes
données_brutes = chargement_brut(10000)

moyenne = pd.DataFrame(données_brutes.groupby(données_brutes[date].dt.year).aggregate({nbretard:"mean", nbprog:"mean"}).reset_index())
moyenne = moyenne.rename(columns={nbretard:retard, nbprog:prog})
moyenne[retardprog] = moyenne[retard]*100/moyenne[prog]

réduit = moyenne
réduit[prog12] = réduit[prog]/12
réduit[retardprog100] = réduit[retardprog]*100
réduit = réduit.drop(prog, axis=1)

col1, col2 = st.columns(2)
st.markdown(
        """
        <style>
            div[data-testid="column"]:nth-of-type(2)
            {
                text-align: right;
            } 
            div[id^="bui-"] > button:nth-child(1) > button:hover {
                background-color: #3DCDBC;
                color:#FAFAFA;
            }
            </style>""",
        unsafe_allow_html=True
    )
with col1:
    titre = "1. Données : TER en retard, TER programmés"
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
                        Selon toi, {Main.r1} % des TER étaient en retard en 2022. Regarde si tu as vu juste ! 👇
                    </body>
                </h5>
                """,
        unsafe_allow_html=True
    )
    st.text("")
    st.markdown(
        """
        <div style = "text-align: center">
            Évolution de la moyenne annuelle de TER en retard, de TER programmés /12 et du rapport "TER en retard/TER programmés" x100 (ressources.data.sncf.com)
        </div>
        """,
        unsafe_allow_html=True
    )
    st.line_chart(réduit, x=date, y=[retard, prog12, retardprog100])
    st.markdown(
        """
        <div style = "text-align: center">
            Évolution de la moyenne annuelle de TER en retard (ressources.data.sncf.com)
        </div>
        """,
        unsafe_allow_html=True
    )
    st.line_chart(moyenne, x=date, y=retard)
with col2:
    Gbouton_s = st.empty()
    Bsuivant = Gbouton_s.button("Suivant ➡️")
    if Bsuivant:
        switch_page("réponse2")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.markdown(
        """
        <div style = "text-align: center">
            Évolution de la moyenne annuelle de TER programmés (ressources.data.sncf.com)
        </div>
        """,
        unsafe_allow_html=True
    )
    st.line_chart(moyenne, x=date, y=prog)
    st.markdown(
        """
        <div style = "text-align: center">
            Évolution de la moyenne annuelle du rapport TER en retard/TER programmés (ressources.data.sncf.com)
        </div>
        """,
        unsafe_allow_html=True
    )
    st.line_chart(moyenne, x=date, y=retardprog)

st.write("Pour plus de plus amples détails, voici les données accessibles également sous forme de tableaux :")
col3, col4, col5 = st.columns(3)
with col4:
    with chart_container(moyenne, ("Graphique", "Tableau", "Tout masquer"), ""):
        st.line_chart(réduit, x=date, y=[retard, prog12, retardprog100])
    with chart_container(moyenne, ("Graphiques", "Tableau", "Tout masquer"), ""):
        st.line_chart(moyenne, x=date, y=retard)
        st.line_chart(moyenne, x=date, y=prog)
        st.line_chart(moyenne, x=date, y=retardprog)