#import libraries
from app_dash.dashboard.settings_plot import *
from app_dash.dashboard.app_dash_standard import *
from math import *

def mask(country,start_date,end_date,month=None):
    if month == None:
        mask = ((df.country == country) & (df["date"] >= start_date)& (df["date"] <= end_date))
    else:
         mask = ((df.country == country) & (df.date_concat==month))

    df_graph = df.loc[mask, :]
    return df_graph


def create_fig_contamination(country,m=None,start_date=None,end_date=None,month=None):
    df_graph = mask(country,start_date,end_date,month)

    liste_col = ["new_cases","new_deaths","cumulative_cases","cumulative_deaths"]
    nb_cols = 2
    # utilisation de ceil et int > évite les divisions par // et donc arrondi au sup
    fig = make_subplots(rows=int(ceil(len(liste_col)/nb_cols)), cols=nb_cols,subplot_titles=("Nouveaux Cas quotidien", "Morts quotidiennes", "Cumul des cas", "Cumul des décès"))

    index_row,index_col,count =1,1,1


    for col in liste_col:
        if count %2 == 0:
            index_col=2
        else:
            index_col=1
            if count>1 :
                index_row+=1
        fig.add_trace(go.Scatter(x=df_graph["date"],y=df_graph[col],name=col.replace("_", " "),marker_color="#f87171",line=dict(width=3)),row=index_row,col=index_col)   
        if m is not None:
            df_graph[f'ma_{col}_{m}']=df_graph[col].rolling(m).mean()
        if count <=2 and month==None:
            df_graph[f'ma_{col}_{m}']=df_graph[col].rolling(m).mean()
            fig.add_trace(go.Scatter(x=df_graph["date"],y=df_graph[f"ma_{col}_{m}"],name=f"moyenne mobile {m} jours",marker_color="#000000",line=dict(width=3)),row=index_row,col=index_col)    
        fig.update_xaxes(title_text="date",row=index_row,col=index_col)
        fig.update_yaxes(title_text="nb", row=index_row, col=index_col)
        count+=1  
        
    theme_graph(fig,1000)     


    return fig



app = DjangoDash(name ='dashboard_callback')
#app.css.append_css({"external_url":"https://storage.googleapis.com/portfolio_django_web_perso/css/app/project/assets/styles.css"})
recup_app(df,app)

@app.callback(
        [Output('daily_plot','figure'),Output('monthly_plot','figure')],
        [Input('country','value'), 
        Input("ma", "value"), 
        Input("month","value"),
        Input("date-range", "start_date"),
        Input("date-range", "end_date")]

)

def display_value(country,m,month,start_date, end_date):
    fig_1 = create_fig_contamination(country=country,m=m,start_date =start_date, end_date = end_date)
    fig_2 = create_fig_contamination(country = country,month = month)
    return fig_1,fig_2




