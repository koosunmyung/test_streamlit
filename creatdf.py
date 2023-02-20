import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly-express
import plost
import numpy as np
import datetime as dt


excel_file = 'F:/strea/STREAM/t_f/test_streamlit/finan.xlsx'
sheet_name = 'pp'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name)
#분기표시
df.기준일= pd.to_datetime(df.기준일)
df['quarter'] = df['기준일'].dt.to_period('Q')
lstday = str(df['기준일'].max(axis=0).year) + "-" + str(df['기준일'].max(axis=0).month)
# print(lstday)
#손익 추출
mask1 = (df['대분류'] != "재무상태") & (df['중분류'] != "기부금") & (df['회계연도'] > 2018)
df = df.loc[mask1]
df['수입비용'] =["수입" if s == "매출" else "비용" for s in df["중분류"]]
for x in df.index: 
    if df.loc[x,'수입비용'] == "수입":
        df.loc[x,'매출']=df.loc[x,'금액']
        # df.loc[x,'영업이익']=df.loc[x,'매출'] + df.loc[x,'비용']
    else:
        df.loc[x,'비용']=df.loc[x,'금액']
df = df.groupby(['회계연도','수입비용', '중분류','보고반영'])[['매출','비용']].sum()

for x in df.index:         
  df.loc[x,'영업이익']=df.loc[x,'매출'] + df.loc[x,'비용']
 

df_base = (df.groupby(['회계연도','수입비용','중분류','보고반영']).sum()/-100000000).round(1)
print(df)
