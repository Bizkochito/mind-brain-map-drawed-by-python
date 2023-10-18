import streamlit as st
import streamlit.components.v1 as components
import random
from streamlit.components.v1 import html
from streamlit_js_eval import streamlit_js_eval
from streamlit_javascript import st_javascript


st.set_page_config(page_title="可编辑脑图", layout="wide")

def printText():
   v = st_javascript(
        "localStorage.getItem('mydate');"
    )
   print(v)

if "textInput" not in st.session_state:
  st.session_state.textInput = ""



p = open("naotu.html", encoding="utf-8")
html_component=components.html(p.read(), height=1000, width=1800, scrolling=True)

with st.sidebar:
  st.button("lalal", on_click=printText)

# with st.sidebar:
#   html('<div id="mydata"></div>')
 # Ajoutez un bouton de soumission avec un label

# Vérifiez si le formulaire a été soumis en utilisant le bouton de soumission
