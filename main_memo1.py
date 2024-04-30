import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#title
st.title("Streamlit 超入門")

st.write("DataFrame")

df = pd.DataFrame({
    "1列目":[1,2,3,4],
    "2列目":[10,20.,30.,40]
})

#st.write(df)

#dataframe 動的な表 縦横等の引数があって変えられる
st.dataframe(df.style.highlight_max(axis=0), width= 400, height=400)
#table　静的な表
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項


```python
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```
"""