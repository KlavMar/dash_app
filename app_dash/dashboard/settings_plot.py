from os import name
from pathlib import Path
from dash import Dash,html,dcc,Input,Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px

dir_csv='csv'
dir_app=Path(__file__).resolve().parent
path=f'{dir_app}/{dir_csv}/'
print(path)

#https://covid19.who.int/WHO-COVID-19-global-data.csv

# contamination sourcing 
df=pd.read_csv(f"{path}covid_world.csv",sep=",")
df.columns = df.columns.str.lower()
df.rename(columns={"date_reported":"date"},inplace=True)
df["date"] = pd.to_datetime(df["date"],format="%Y-%m-%d")
df_world = df.groupby('date').agg("sum")
df_world=df_world.reset_index()
df_world["date"] = pd.to_datetime(df_world["date"],format="%Y-%m-%d")
df_world["country"]="World"
df = pd.concat([df,df_world])
df["month"]=pd.to_datetime(df.date,format="%m").dt.month_name()
df["year"]=df.date.dt.year
df["date_concat"]=df.month.astype(str) +" " + df.year.astype(str)