from trucs_utiles import *
import Main
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
c1, c2, c3 = st.columns(3)
with c2:
    question = "3. Selon vous, suite de la question un peu longue ?"
    zoneQuestion = mise_en_forme_Question(question)
    zoneText_input = st.empty()
    Main.r3 = zoneText_input.text_input("Votre réponse ?")
    boutons_rs("question2", "réponse1", zoneQuestion, zoneText_input, "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNWI1MzEyODlhODViMGNjZjE0ZDE0NWYzZTY5MGU4YzhjOTRkMGJjOSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/hq8MAOMhX3iIYjqcSk/giphy.gif")



