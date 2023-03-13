import pandas as pd
import plotly.express as px
from pandas_datareader import wb

#from jupyter_dash import JupyterDash
from dash import dcc, html, Dash
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

# import os
# os.chdir("C:/Users/DELL/Desktop/ban438/workshop/co2_explorer/")
data = pd.read_csv("world_1960_2021.csv")
#data['year'] = pd.to_datetime(data['year'])
data.set_index('year', inplace = True)
data.dropna(inplace= True)
data.head()

#line graph for total co2
fig_co2 = px.line(
    data,
    y = 'EN.ATM.CO2E.KT'
)

fig_co2.update_layout(
    yaxis_title = None,
    xaxis_title = None,
    title = "Total CO2 emission overtime",
    title_x = 0.5,   
    margin = {'l' : 0, 'r' : 0}
)
#line graph for co2 per capita
fig_co2pc = px.line(
    data,
    y = 'EN.ATM.CO2E.PC'
)

fig_co2pc.update_layout(
    yaxis_title = None,
    xaxis_title = None,
    title = "Total CO2 emission Per Capita overtime",
    title_x = 0.5,   
    margin = {'l' : 0, 'r' : 0}
)

dbc_css = 'https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css'
load_figure_template('bootstrap')

app = Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP, dbc_css])
server = app.server

app.layout = dbc.Container(
    children = [
        
        # Header
        html.H1('CO2 emissions around the world'),
        dcc.Markdown(
            """Data on emissions and potential drivers are extracted from the 
               [World Development Indicators](https://datatopics.worldbank.org/world-development-indicators/) 
               database."""
        ),
        dcc.Graph(figure = fig_co2)
    ],
    className = 'dbc'
)

app.run_server()
if __name__ == '__main__': 
    app.run_server(debug = True)
