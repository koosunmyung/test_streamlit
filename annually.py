import streamlit as st  # pip install streamlit
import pandas as pd  # pip install pandas
import plotly.express as px  # pip install plotly-express
import plost
import numpy as np
import datetime as dt
from creatdf import df_base
from creatdf import lstday


st.set_page_config(page_title="년도별 손익", page_icon=":bar_chart:", layout="centered")

# quarter = df_base['quarter'].unique().tolist()
# quarter_selection = st.slider('분기선택:', 
#                                 min_value= min(quarter),
#                                 max_value= max(quarter),
#                                 value=(min(quarter),max(quarter)))
# number_of_result = df[mask].shape[0]
# st.markdown(f'*Available Results: {number_of_result}*')                                         
# age_selection = st.slider('Age:',
#                         # min_value= min(ages),
#                         # max_value= max(ages),
#                         # value=(min(ages),max(ages)))
#                         value=(min_value, max_value))


# excel_file = 'F:/strea/STREAM/dbd_ex/finan.xlsx'
# sheet_name = 'pp'

# df = pd.read_excel(excel_file,
#                    sheet_name=sheet_name)
# #분기표시
# df.기준일= pd.to_datetime(df.기준일)
# df['quarter'] = df['기준일'].dt.to_period('Q')

# #손익 추출
# mask1 = (df['대분류'] != "재무상태") & (df['중분류'] != "기부금")
# df = df.loc[mask1]
# df['수입비용'] =["수입" if s == "매출" else "비용" for s in df["중분류"]]
# for x in df.index: 
#     if df.loc[x,'수입비용'] == "수입":
#         df.loc[x,'매출']=df.loc[x,'금액']
#         # df.loc[x,'영업이익']=df.loc[x,'매출'] + df.loc[x,'비용']
#     else:
#         df.loc[x,'비용']=df.loc[x,'금액']
# df = df.groupby(['회계연도','수입비용', '중분류','보고반영'])[['매출','비용']].sum()

# for x in df.index:         
#   df.loc[x,'영업이익']=df.loc[x,'매출'] + df.loc[x,'비용']
 
# # df.to_excel('C:/CODING/Streamlit/dashboard_ex/test00.xlsx')
# # df = df.groupby(df(['회계연도','R','C','중분류','세분류','전기월','보고반영']))
# # df_b = (df.groupby(['회계연도'])[['매출','비용', '중분류', '수입비용', '보고반영','금액']].sum()/-100000000).round(1)
# df_b = (df.groupby(['회계연도','수입비용','중분류','보고반영']).sum()/-100000000).round(1)
# df_base.to_excel('F:/strea/STREAM/dbd_ex/test0.xlsx')
 

# 연도별 손익요약(수입,비용,영업이익) 재구성
df_b = df_base.reset_index()# df_b = (df.groupby(['회계연도'])[['매출','비용', '중분류', '수입비용', '보고반영','금액']].sum()/-100000000).round(1)
print(df_b)
# df_b2 = (df.groupby(['회계연도','매출','비용', '영업이익', '보고반영']).sum()/-100000000).round(1)
# df_c.to_excel('C:/CODING/Streamlit/dashboard_ex/test.xlsx')
# mask = (df_base['quarter'].between(*quarter_selection))
df_ann = df_b.groupby(['회계연도'])['매출','비용', '영업이익', '보고반영'].sum()
df_ann = df_ann.reset_index()
df_ann=pd.melt(df_ann,id_vars=['회계연도'],value_vars= ['매출','비용','영업이익'])
# df_base.to_excel('F:/strea/STREAM/dbd_ex/test11.xlsx')

st.caption(f"기준년월 : {lstday}")
fig = px.bar(df_ann, x="회계연도", y="value", color="variable", barmode='group', text_auto=True , template="plotly_dark",width=400, height=600,
color_discrete_map={
        '매출': 'blue',
        '비용': 'teal',
        '영업이익':'red'})

st.plotly_chart(fig)
