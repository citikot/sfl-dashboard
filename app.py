import streamlit as st
import pandas as pd
from PIL import Image


def switch_chart_data(per, data):
    return 'database/sfl_' + data + '_' + per + '_db_for_dashboard.parquet.gzip'


st.set_page_config(layout="wide")

st.sidebar.header("SFL game statistics test dashboard")
img = Image.open("img/black_market.3bde9316.jpg")
st.sidebar.image(img, width=300)

# basic config
period = ['daily', 'weekly', 'monthly']
data_files = ['all_trans', 'new_accounts']
data_cols = ['transactions', 'new_accounts']
cols_num = 2
col_headers = ['Transactions amount per period', 'New accounts per period']

st.subheader('Basic data')
chart_period = st.select_slider('Please, select a period for reflection', period)

# reflection of charts
cols = st.columns((1, 1))
for i in range(0, cols_num):
    with cols[i].container():
        st.subheader(col_headers[i])
        db_file = switch_chart_data(chart_period, data_files[i])
        df = pd.read_parquet(db_file)
        st.bar_chart(df[data_cols[i]], use_container_width=True)

