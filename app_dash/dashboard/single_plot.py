from app_dash.dashboard.settings_plot import *



data_frame = df[df.country=="France"]

fig = px.bar(data_frame=data_frame,x="date",y="new_cases",color_discrete_sequence=["#06b6d4"])
fig.update_layout(
font=dict( family="Arial Black",size=18,color="#6b7280"),
title="Nouveaux Cas",
showlegend=False,paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)"
)


app = DjangoDash(name ='single_plot')

app.layout=html.Div([
    html.Div(
        children = [
        html.H3(children="Nouveaux Cas en France")
            
        ]),
        html.Div([
            dcc.Graph(id="news_cases",figure=fig,style={"height":"500px","width":"750px","margin":"1em"})
        ])
])


