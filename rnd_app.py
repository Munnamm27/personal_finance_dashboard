import numpy as np
import plotly.express as px
import dash
from dash import dcc, html, dash_table, callback_context, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from datetime import date
import pandas as pd

df=pd.read_excel("records.xlsx")

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)




app.layout = dbc.Container(
    [
        dbc.Row( 
            [ 
                dcc.Input(id='val_1',type='text'),
                dcc.Input(id='val_2',type='number'),
                html.Div(id='out')
            ]
        )

    ],
    fluid=True,style={'backgroundColor':'#EAF5FF'}
)


@app.callback( 
    Output('out','children'),
    Input('val_1','value'),
    Input('val_2','value')
    
)

def write(v1,v2):
    pd.DataFrame().to_excel('records.xlsx',index=False)
    return html.H4("excel created")



if __name__ == "__main__":
    app.run_server(debug=True, port=8000)

