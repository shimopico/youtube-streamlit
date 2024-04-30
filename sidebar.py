import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

st.title("Streamlit 超入門")

st.sidebar.write("Fan Fan Image")

"--------------------------------------------------------------------"
text = st.sidebar.text_input("あなたの趣味を教えてください")
condition = st.sidebar.slider("あんたの今の調子は", 0, 100, 50)

"あなたの趣味は", text , "です"
"コンディション:" , condition
