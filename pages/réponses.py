from datetime import *
import pandas as pd
import streamlit as st
import plotly.tools
from pandas import to_datetime
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.chart_container import chart_container
import time
from trucs_utiles import *

st.set_page_config(layout="wide")
titre = "1. Données : trains en retard, trains programmés"
mise_en_forme_Question(titre)

date = "Date"
fichier = "regularite-mensuelle-ter.csv"
nbretard = "Nombre de trains en retard en définitive"
retard = "Retards"
nbprog = "Nombre de trains programmés"
prog = "Trains programmés"
prog12 = "Trains programmés /12"
retardprog = "Retard/programmés (%)"
retardprog100 = "Retard/programmés x100 (%)"

@st.cache_data
def chargement_brut(nb_lignes):
    données_brutes = pd.read_csv(fichier, delimiter=";", nrows=nb_lignes)
    données_brutes["Date"] = pd.to_datetime(données_brutes["Date"])
    return données_brutes

données_brutes = chargement_brut(10000)

moyenne = pd.DataFrame(données_brutes.groupby(données_brutes[date].dt.year).aggregate({nbretard:"mean", nbprog:"mean"}).reset_index())
moyenne = moyenne.rename(columns={nbretard:retard, nbprog:prog})
moyenne[retardprog] = moyenne[retard]*100/moyenne[prog]

réduit = moyenne
réduit[prog12] = réduit[prog]/12
réduit[retardprog100] = réduit[retardprog]*100
réduit = réduit.drop(prog, axis=1)

col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        <div style = "text-align: center">
            Évolution de la moyenne annuelle de TER en retard, de TER programmés /12 et du rapport TER en retard/TER programmés x100
        </div>
        """,
        unsafe_allow_html=True
    )
    st.line_chart(réduit, x=date, y=[retard, prog12, retardprog100])
    st.markdown(
        """
        <div style = "text-align: center">
            Évolution de la moyenne annuelle de TER en retard
        </div>
        """,
        unsafe_allow_html=True
    )
    st.line_chart(moyenne, x=date, y=retard)
with col2:
    st.markdown(
        """
        <div style = "text-align: center">
            Évolution de la moyenne annuelle de TER programmés
        </div>
        """,
        unsafe_allow_html=True
    )
    st.line_chart(moyenne, x=date, y=prog)
    st.markdown(
        """
        <div style = "text-align: center">
            Évolution de la moyenne annuelle du rapport TER en retard/TER programmés
        </div>
        """,
        unsafe_allow_html=True
    )
    st.line_chart(moyenne, x=date, y=retardprog)

col3, col4, col5 = st.columns(3)
with col4:
    with chart_container(moyenne, ("Graphique", "Tableau", "Tout masquer"), ""):
        st.line_chart(réduit, x=date, y=[retard, prog12, retardprog100])
    with chart_container(moyenne, ("Graphiques", "Tableau", "Tout masquer"), ""):
        st.line_chart(moyenne, x=date, y=retard)
        st.line_chart(moyenne, x=date, y=prog)
        st.line_chart(moyenne, x=date, y=retardprog)