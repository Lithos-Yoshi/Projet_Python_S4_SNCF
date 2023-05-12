import streamlit as st
import streamlit_extras as ste
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
import numpy as np
from pathlib import Path
import httpx
from pydantic import BaseModel, HttpUrl
from streamlit.runtime.uploaded_file_manager import UploadedFile
import time
import base64


#st.title('Quiz SNCF')
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"gif"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

groupe1 = st.empty()

c1, c2, c3 = st.columns(3)
with c1:
    st.text('')
with c2:
    test1 = st.markdown("<h1 style='text-align: center'>Quiz SNCF</h1>", unsafe_allow_html=True)
with c3:
    st.text('')
test2 = groupe1.button("Commencer")
if test2:
    test1.empty()
    groupe1.empty()
    html = """<video controls width="1920" height="1080" autoplay="true" muted="true" loop="false">
<source
            src="https://clipchamp.com/watch/kFDbIGrzyke"
            type="video/mp4" />
</video>"""
    st.markdown(html, unsafe_allow_html=True)

    time.sleep(7.5)
    switch_page("p1")





# use_example = "Example OpenAPI Specification"
# use_upload = "Upload an OpenAPI Specification"
# use_text_input = "Enter OpenAPI Specification in Text Input"
# use_url = "Fetch OpenAPI Specification from a URL"
#
# st.header('OAS -> Pydantic -> Streamlit Form Code Generator')
# input_method = st.selectbox(
#     label="How will you select your API Spec",
#     options=[use_example, use_upload, use_text_input, use_url],
# )
#
# st.subheader(input_method)
#
#
# @st.cache_data
# def decode_uploaded_file(oas_file: UploadedFile) -> str:
#     return oas_file.read().decode()
#
# @st.cache_data
# def decode_text_from_url(oas_url: str) -> str:
#     try:
#         response = httpx.get(oas_url, follow_redirects=True, timeout=10)
#         return response.text
#     except Exception as e:
#         print(repr(e))
#         return ""
#
# class ValidURL(BaseModel):
#     url: HttpUrl
#
# def get_raw_oas(input_method: str) -> str:
#     if input_method == use_example:
#         st.write("This will demo how the app works!")
#         oas_file = Path("quote-oas.json")
#         raw_oas = oas_file.read_text()
#     elif input_method == use_upload:
#         st.write("This will let you use your own JSON or YAML OAS!")
#         oas_file = st.file_uploader(
#             label="Upload an OAS",
#             type=["json", "yaml", "yml"],
#             accept_multiple_files=False,
#         )
#         if oas_file is None:
#             st.warning("Upload a file to continue!")
#             st.stop()
#         raw_oas = decode_uploaded_file(oas_file)
#     elif input_method == use_text_input:
#         st.write("This will parse raw text input into JSON or YAML OAS!")
#         raw_oas = st.text_area(label="Enter OAS JSON or YAML text")
#         if not len(raw_oas):
#             st.warning("Enter OAS text to continue!")
#             st.stop()
#     elif input_method == use_url:
#         st.write("This will fetch text from the URL containing a JSON or YAML OAS!")
#         raw_oas_url = st.text_input(label="Enter the URL that hosts the OAS")
#         try:
#             oas_url = ValidURL(url=raw_oas_url)
#         except Exception as e:
#             print(repr(e))
#             st.warning("Enter a valid HTTP(S) URL to continue!")
#             st.stop()
#         raw_oas = decode_text_from_url(oas_url.url)
#     else:
#         raise Exception("Unknown input_method")
#     return raw_oas
#
# raw_oas = get_raw_oas(use_upload)
# with st.expander("Show input OAS"):
#     st.code(raw_oas)






DATE_COLUMN = "regularite-mensuelle-ter.csv"
FICHIER_DONNÉES = "regularite-mensuelle-ter.csv"

@st.cache_data
def load_data(nb_lignes):
    data = pd.read_csv(FICHIER_DONNÉES, delimiter=";", nrows=nb_lignes)
    return data






#st.subheader('Number of pickups by hour')
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)

# Some number in the range 0-23
#hour_to_filter = st.slider('hour', 0, 23, 17)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)


police = """
			<style>
			@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap');

			html, body, [class*="css"]  {
			
			font-family: 'Poppins', sans-serif;
			}
			</style>
			"""
st.markdown(police, unsafe_allow_html=True)
