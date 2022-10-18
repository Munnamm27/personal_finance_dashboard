import numpy as np
import plotly.express as px
import dash
from dash import dcc, html, dash_table, callback_context, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from datetime import date
import pandas as pd
import style as stl

df = pd.read_excel("records.xlsx")

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.LITERA],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

header = dbc.Row(html.H1("Header", className="text-center text-bold", style=stl.header))


expense_col = dbc.Col(
    [
        html.H3("Expense Section"),
        html.H6("Category"),
        dcc.Input(
            id="category", type="text", placeholder="Enter Category", style=stl.inp
        ),
        html.H6("Product"),
        dcc.Input(
            id="product", type="text", placeholder="Enter Product", style=stl.inp
        ),
        html.H6("Price"),
        dcc.Input(id="price", type="number", placeholder="Enter Price", style=stl.inp),
        dbc.Row(
            [
                dbc.Col(dbc.Button("Add", id="add-i", n_clicks=0)),
                dbc.Col(
                    dbc.Button(
                        "Remove", id="remove_last-i", n_clicks=0, className="btn-danger"
                    )
                ),
                dbc.Col(
                    dbc.Button(
                        "Submit", id="submit-i", n_clicks=0, className="btn-success"
                    )
                ),
            ],
            align="center",
            justify="center",
        ),
    ],
    style=stl.section,
)

income_col = dbc.Col(
    [
        html.H3("Income Section"),
        html.H6("Account"),
        dcc.Dropdown(
            id="acc",
            options=["IBBL-1", "IBBL-2", "SCB", "Cash Out"],
            placeholder="Select Account",
            style=stl.inp,
        ),
        html.H6("Amount"),
        dcc.Input(
            id="ibbl_2", type="number", placeholder="Enter Amount", style=stl.inp
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Button("Add", id="add-e", n_clicks=0)),
                dbc.Col(
                    dbc.Button(
                        "Remove", id="remove_last-e", n_clicks=0, className="btn-danger"
                    )
                ),
                dbc.Col(
                    dbc.Button(
                        "Submit", id="submit-e", n_clicks=0, className="btn-success"
                    )
                ),
            ],
            align="center",
            justify="center",
        ),
    ],
    style=stl.section,
)

budget_col = dbc.Col(
    [
        html.H3("Budget Section"),
        html.H6("Section for Budget"),
        dcc.Input(
            id="budget_cat",
            type="number",
            placeholder="Select Budget Category",
            style=stl.inp,
        ),
        html.H6("Budget amount"),
        dcc.Input(
            id="budget_amount",
            type="number",
            placeholder="Set Budget amount",
            style=stl.inp,
        ),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Button(
                        "Add",
                        id="add-b",
                        n_clicks=0,
                        style={"backgorundColor": "red"},
                    )
                ),
                dbc.Col(
                    dbc.Button(
                        "Remove", id="remove_last-b", n_clicks=0, className="btn-danger"
                    )
                ),
                dbc.Col(
                    dbc.Button(
                        "Submit", id="submit-b", n_clicks=0, className="btn-success"
                    ),
                ),
            ],
            align="center",
            justify="center",
        ),
    ],
    style=stl.section,
)

preview_col = dbc.Col(
    [   
        dbc.Row([
        html.H4("Input Preview",className='text-center'),
        dcc.Graph(id="final_tbl",style=stl.fig),
        html.Label("msg",className='text-center')
    ],style=stl.section),

    dbc.Row( 
        [ 
            html.H4("Data Preview",className='text-center'),
            dbc.Col(dcc.Graph(id='expns-tbl'),md=6),
            dbc.Col(dcc.Graph(id='income-tbl'),md=6)
        ],style=stl.section
    )

    ],
    width={"size": 8, "offset": 0, "order": 2}
)




app.layout = dbc.Container(
    [
        header,
        dbc.Row(
            [
                dbc.Col(
                    [expense_col, income_col, budget_col],
                    width={"size": 3, "offset": 0, "order": 1},
                ),
                preview_col,
            ],
            align="left",
            justify="center",
        ),
    ],
    fluid=True,
    style={
        "backgroundColor": "#ffe9fb",
        "border": "3px black solid",
        "border-radius": "5px",
    },
)


# @app.callback(
#     Output('out','children'),
#     Input('val_1','value'),
#     Input('val_2','value')

# )

# def write(v1,v2):

#     return html.H4("excel created")


if __name__ == "__main__":
    app.run_server(debug=True, port=8000)
