import streamlit as st
import pandas as pd
from PIL import Image


def switch_chart_data(per):
    if per == "daily":
        return "database/sfl_all_trans_daily_db_for_dashboard.parquet.gzip"
    elif per == "weekly":
        return "database/sfl_all_trans_weekly_db_for_dashboard.parquet.gzip"
    elif per == "monthly":
        return "database/sfl_all_trans_monthly_db_for_dashboard.parquet.gzip"


st.set_page_config(layout="wide")
st.sidebar.header("SFL game statistics test dashboard")
img = Image.open("img/black_market.3bde9316.jpg")
st.sidebar.image(img, width=300)

st.title("Transactions amount chart")
period = ['daily', 'weekly', 'monthly']
chart_period = st.select_slider('Choose period', period)
db_file = switch_chart_data(chart_period)
df = pd.read_parquet(db_file)

with st.container():
    st.bar_chart(df['transactions'], use_container_width=True)
