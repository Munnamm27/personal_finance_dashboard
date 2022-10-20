import numpy as np
import plotly.express as px
import dash
from dash import dcc, html, dash_table, callback_context, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
import style as stl
import dropdown_list as dlist
import graphs
import dataloader as dl

expense_col = dbc.Col(
    [
        html.H3("Expense Section"),
        html.H6("Category"),
        dcc.Dropdown(
            id="category", options=dlist.category, placeholder="Enter Category", style=stl.inp
        ),
        html.H6("Product"),
        dcc.Input(
            id="product", type="text", placeholder="Enter Product", style=stl.inp
        ),
        html.H6("Cost"),
        dcc.Input(id="price", type="number", placeholder="Enter Cost", style=stl.inp),
        dbc.Row(
            [
                dbc.Col(dbc.Button("Add", id="add-i", n_clicks=0)),
                dbc.Col(
                    dbc.Button(
                        "Remove", id="remove-i", n_clicks=0, className="btn-danger"
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
            id="account",
            options=["IBBL-1", "IBBL-2", "SCB", "Cash Out"],
            placeholder="Select Account",
            style=stl.inp,
        ),
        html.H6("Source"),
        dcc.Dropdown(
            id="source",
            options=["Salary", "Abbu", "Gifts"],
            placeholder="Select Source",
            style=stl.inp,
        ),
        html.H6("Amount"),
        dcc.Input(
            id="amount", type="number", placeholder="Enter Amount", style=stl.inp
        ),
        dbc.Row(
            [
                dbc.Col(dbc.Button("Add", id="add-e", n_clicks=0)),
                dbc.Col(
                    dbc.Button(
                        "Remove", id="remove-e", n_clicks=0, className="btn-danger"
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
        dcc.Dropdown(
            id="budget_cat",
            options=dlist.budget_list,
            placeholder="Select Budget Category",
            style=stl.inp,
        ),
        html.H6("Budget amount"),
        dcc.Input(
            id="budget_amm",
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
                        "Remove", id="remove-b", n_clicks=0, className="btn-danger"
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

budget_preview = dbc.Row(
    [   
        dbc.Col(
        dbc.Button(
            "See Budgets",
            id="see-budget-button",
            className="mb-3",
            color="primary",
            n_clicks=0,
        ),md=2),
        dbc.Col(
        dbc.Collapse(
            html.Div(graphs.get_small_tbl(dl.df_budget)),
            id="budget-preview",
            is_open=False,
        ),md=6),
    ],align='left',justify='center'
)

preview_col = dbc.Col(
    [
        dbc.Row(
            [
                html.H4("Input Preview", className="text-center"),
                html.Div(
                    id="input-tbl",
                    style={
                        "textAlign": "center",
                        "paddingLeft": "100px",
                        "paddingRight": "100px",
                    },
                ),
            ],
            align="left",
            justify="center",
            style=stl.sectionh,
        ),
        dbc.Row(
            [
                html.H4("Data Preview", className="text-center"),
                html.H6("Expense Table", className="text-center"),
                html.Div(id="expense-tbl"),
                html.H6("Income Table", className="text-center"),
                html.Div(id="income-tbl"),
            ],
            style=stl.section,
        ),

    budget_preview
    ],
    width={"size": 8, "offset": 0, "order": 2},
)



input_tab = dbc.Row(
    [
        dbc.Col(
            [expense_col, income_col, budget_col],
            width={"size": 3, "offset": 0, "order": 1},
        ),
        preview_col,
        
    ],
    align="left",
    justify="center",
)