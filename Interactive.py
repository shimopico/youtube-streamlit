import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.title("Streamlit 超入門")

st.write("Display Image")

option = st.selectbox(
    "あなたが好きな数字を教えてください、",
    list(range(1,11))
)
"あなたの好きな数字は、", option, "です!"

"--------------------------------------------------------------------"
#true false の変化に応じて表示できる
if st.checkbox("Show Image"):
    img = Image.open("saizeriya.png")
    st.image(img, caption= "saize", use_column_width=True)

"--------------------------------------------------------------------"
text = st.text_input("あなたの趣味を教えてください")
"あなたの趣味は", text , "です"

"--------------------------------------------------------------------"

condition = st.slider("あんたの今の調子は", 0, 100, 50)
"コンディション:" , condition
