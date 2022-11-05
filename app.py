import streamlit as st
import pandas as pd
import plotly.express as px


st.image("https://hololive.hololivepro.com/wp-content/themes/hololive/images/ogp.jpg") 

st.title('Hololive Indonesia Super Chat Analysis')
st.markdown(
    '''
    Untuk analisis lebih detail mengenai Vtuber dan Super Chat nya bisa cek di [tweet ini](https://twitter.com/shandytepe/status/1585567017884876800)
    ''')

@st.cache()
def load_data():
    df = pd.read_csv('sc-holo-id-data.csv')
    return df

df = load_data()

name = df['englishName'].unique()

vtuber_choices = st.selectbox('Pilih Vtuber: ', name)

tmp = df[df['englishName'] == vtuber_choices]

title = st.write("Super Chat", vtuber_choices, "from", min(df['period'][df['englishName'] == vtuber_choices]), \
                "s.d", max(df['period'][df['englishName'] == vtuber_choices]))

fig = px.line(tmp, x='period', y='totalSC_IDR_clean', title=title).update_layout(xaxis_title="Period", yaxis_title="Total Super Chat IDR")

st.plotly_chart(fig, use_container_width=True)

new_df = df[df['englishName'] == vtuber_choices][['totalSC_IDR_clean','period']]

new_df.columns = ["Total SC IDR", "Period"]

st.write("More detailed dataset (kind off...)")

st.dataframe(new_df, use_container_width=True)
