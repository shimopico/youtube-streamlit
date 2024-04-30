import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#title
st.title("Streamlit 超入門")

st.write("DataFrame")

df = pd.DataFrame(
    np.random.rand(20,3),
    columns= ["a", "b", "c"]
    )

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

#[35.69, 139.70]座標に乱数値を入力してmap
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69, 139.70],
    columns = ["lat", "lon"]
)
st.map(df)

from PIL import Image

st.write("Display Image")

img = Image.open("saizeriya.png")
#use_column_width　サイズに合わせて変更
st.image(img, caption= "saize", use_column_width=True)