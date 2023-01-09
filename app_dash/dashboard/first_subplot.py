#import libraries
from app_dash.dashboard.settings_plot import *
from math import *


style_graph={"background":"#ffffff"}
liste_col = ["new_cases","new_deaths","cumulative_cases","cumulative_deaths"]
nb_cols = 2
# utilisation de ceil et int > évite les divisions par // et donc arrondi au sup
fig = make_subplots(rows=int(ceil(len(liste_col)/nb_cols)), cols=nb_cols,subplot_titles=("Nouveaux Cas quotidien", "Morts quotidiennes", "Cumul des cas", "Cumul des décès"))
data_frame = df[df.country=="France"]
index_row,index_col,count =1,1,1


for col in liste_col:
    if count %2 == 0:
        index_col=2
    else:
        index_col=1
        if count>1 :
            index_row+=1
    fig.add_trace(go.Scatter(x=data_frame["date"],y=data_frame[col],name=col.replace("_", " "),marker_color="#f87171",line=dict(width=3)),row=index_row,col=index_col)      
    fig.update_xaxes(title_text="date",row=index_row,col=index_col)
    fig.update_yaxes(title_text="nb", row=index_row, col=index_col)
    count+=1  
    
fig.update_layout(
font=dict( family="Arial Black",size=18,color="#6b7280"),height=1000,
title="Nouveaux Cas",
showlegend=False,paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)"
)



app = DjangoDash(name ='first_dashboard')

app.layout=html.Div([
        html.Div(
                children = [
                        html.H3(children="Visualisation des contaminations en France",style={"font-size":"2em","color":"#991b1b"})
                ]), 
        html.Div([dcc.Graph(id="monthly_plot",figure=fig,style=style_graph)]),
        ])







