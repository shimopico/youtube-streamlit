import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.title("Streamlit 超入門")

st.write("Fan Fan Image")

left_column, righit_column = st.columns(2)
button = left_column.button("右カラムに文字を表示")
if button:
    righit_column.write("ここは右カラムです")

expander = st.expander("問い合わせ")
expander.write("問い合わせ内容を書く")


text = st.text_input("あなたの趣味を教えてください")
condition = st.sidebar.slider("あんたの今の調子は", 0, 100, 50)

"あなたの趣味は", text , "です"
"コンディション:" , condition
