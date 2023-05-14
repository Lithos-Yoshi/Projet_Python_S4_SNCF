from datetime import *
import pandas as pd
import streamlit as st
import plotly.tools
from pandas import to_datetime
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.chart_container import chart_container
import time

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

with chart_container(moyenne, ("Graphique", "Tableau", "Tout masquer"), ""):
    st.line_chart(réduit, x=date, y=[retard, prog12, retardprog100])

with chart_container(moyenne, ("Graphiques", "Tableau", "Tout masquer"), ""):
    st.line_chart(moyenne, x=date, y=retard)
    st.line_chart(moyenne, x=date, y=prog)
    st.line_chart(moyenne, x=date, y=retardprog)