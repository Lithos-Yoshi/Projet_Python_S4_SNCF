from trucs_utiles import *
import Main
st.markdown(
         f"""
         <style>
            .stApp {{
                background-color: #3DCDBC;
                background-attachment: fixed;
                background-size: cover
            }}
         </style>
        """,
        unsafe_allow_html=True
    )
c1, c2, c3 = st.columns(3)
with c2:
    question = "2. Quel est le pourcentage de Français(es) satisfait(e)s de la ponctualité de la SNCF en 2022 ?"
    zoneQuestion = mise_en_forme_Question(question)
    zoneText_input = st.empty()
    Main.r2 = zoneText_input.text_input("Votre réponse ?")
    boutons_rs("question1", "question3", zoneQuestion, zoneText_input, "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNjgyNjRjZmE4ZGExYzlkMTZiZTM0NzMxNDAwMTM4MjliOTgzNTZiMSZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/kDAX9gEXsKJbCWBNnj/giphy.gif")


