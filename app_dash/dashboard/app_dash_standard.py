from dash import Dash,html,dcc,Input,Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash



style_default={ "width":"20em", "color":"#991b1b","font-weight":"700"}

style_tab={"background":"#991b1b","color":"#ededed","font-weight":"700","border-radius":"0.25em", "margin":"0.5em 0.25em","padding":"1em"}
selected_tab={'background':"white","color":"#991b1b","font-weight":"700","border-radius":"0.25em","margin":"0.5em 0.25em","padding":"1em","border-style":"none"}
style_nav={
    "display":"flex",
     "padding":"1em",
     "margin":"1em auto",
     "justify-content":"space-around",
     "align-items":"center",
     "background":"#991b1b",
     "color":"#991b1b",
     "border-radius":"0.5em"
}
style_graph={
    "margin":"auto","box-shadow":"0.5em 0.5em 0.75em #d1d5db,-0.5em -0.5em 0.75em #d1d5db","width":"95%","border-radius":"1em","background":"#ffffff","min-height":"1000px"
}
def theme_graph(fig,height):

    fig.update_layout(font=dict( family="Arial Black",size=18,color="#6b7280"),height=height,showlegend=False)
    fig.update_xaxes(showgrid=False)
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)",plot_bgcolor="rgba(0,0,0,0)",margin=dict(l=20, r=20, t=100, b=20))

    return fig
    
def recup_app(df,app):
    app.layout=html.Div([
        html.Div(
                children = [
                        html.H3(children="Pays",style={"color":"#991b1b"}),
                        dcc.Dropdown(id="country",options =[{'label':i, 'value':i } for i in sorted(df.country.unique())],value="France",)
                    ],
                style=style_default
                ),
    dcc.Tabs([
        
        #begin tab
        dcc.Tab(label='Evolution depuis le début et à date', children=[
            # begin nac
            html.Div([
        
                html.Div(
                children = [
                    html.H3(children="Date",style={"color":"white"}),
                    dcc.DatePickerRange(id="date-range",display_format="DD-MM-Y",min_date_allowed=df['date'].min().date(),max_date_allowed=df['date'].max().date(),start_date=df['date'].min().date(),end_date=df['date'].max().date())
                ]
                ),
            html.Div(
                children=[
                    html.H3(children="Moyenne mobile", style={"color":"white"}),
                    dcc.Dropdown(id="ma",options =[{'label':i, 'value':i } for i in range(0,60,10)],value=10)
                ]
                )],
            style=style_nav,className="header-nav"),
            # end nav 
            html.Div([dcc.Graph(id="daily_plot",style=style_graph)])
        ],style=style_tab,selected_style=selected_tab),
        #end tab One 

        #begin tab

        dcc.Tab(label='Evolution Mois par Mois', children=[
            html.Div([
                
                html.Div(
                    children=[
                        html.H3(children="Mois",style={"color":"white"}),
                        dcc.Dropdown(id="month",options = [{'label':i,"value":i } for i in df.sort_values(by="date").date_concat.unique()],value=df.sort_values(by="date").date_concat.unique()[-1])
                        ],style=style_default
                        ),
            ],style=style_nav,className="header-nav"),    
            html.Div([dcc.Graph(id="monthly_plot",style=style_graph)]),
        ],style=style_tab,selected_style=selected_tab)
        #end tab
            
        ])
    ])



    return app