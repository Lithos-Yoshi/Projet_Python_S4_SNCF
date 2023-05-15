from trucs_utiles import *
import Main
st.markdown(
         f"""
         <style>
            .stApp {{
                background-color: #39342E;
                background-attachment: fixed;
                background-size: cover
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

c1, c2, c3 = st.columns(3)
with c2:
    question = "1. Quelle est le rapport moyen trains en retard / trains programmés en 2022 (en %) ?"
    zoneQuestion = mise_en_forme_Question(question)
    zoneText_input = st.empty()
    Main.r1 = zoneText_input.text_input("Votre estimation :")
    boutons_rs("Main", "question2", zoneQuestion, zoneText_input, "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTgyMzkzMDA4YzRiZTE2YjZjNzgwZDdkZGFjZmU4YTQ0Y2IxZTdkZiZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/S9LlBCXDfBHQZ34cHH/giphy.gif")



