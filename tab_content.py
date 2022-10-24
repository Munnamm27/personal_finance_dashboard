from click import style
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


########### TAB INPUT ##################################


expense_col = dbc.Col(
    [
        html.H3("Expense Section"),
        html.H6("Category"),
        dcc.Dropdown(
            id="category",
            options=dlist.category,
            placeholder="Enter Category",
            style=stl.inp,
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
            ),
            md=2,
        ),
        dbc.Col(
            dbc.Collapse(
                html.Div(graphs.get_small_tbl(dl.df_budget)),
                id="budget-preview",
                is_open=False,
            ),
            md=6,
        ),
    ],
    align="left",
    justify="center",
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
        budget_preview,
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

######################################### TAB Vis ###########################################


card_row = dbc.Col(
    [
        html.H6("Balance Status", className="text-center"),
        dbc.Row(
            [
                dbc.Col(
                    graphs.get_card("Spent", 7000, "assets/dollar.png"),
                    md=2,
                    style=stl.section_card,
                ),
                dbc.Col(
                    graphs.get_card("Available", 7000, "assets/tk_logo_1.jpeg"),
                    md=2,
                    style=stl.section_card,
                ),
                dbc.Col(
                    graphs.get_card("Bank 1", 7000, "assets/scb.png"),
                    md=2,
                    style=stl.section_card,
                ),
                dbc.Col(
                    graphs.get_card("Bank 2", 7000, "assets/ibbl.png"),
                    md=2,
                    style=stl.section_card,
                ),
                dbc.Col(
                    graphs.get_card("Cash", 7000, "assets/cash_in_hand.png"),
                    md=2,
                    style=stl.section_card,
                ),
            ],
            align="center",
            justify="center",
        ),
    ],
    style=stl.section,
)

###########temp var############
label = [
    "Oxygen",
    "Hydrogen",
    "Carbon_Dioxide",
    "Nitrogen",
    "Carbon",
    "Oxaygen",
    "Hydroagen",
    "Carboan_Dioxide",
    "Nitraogen",
    "Caarbon",
    "e",
]
values = [4500, 2500, 1053, 500, 200, 4500, 2500, 1053, 500, 200, 900]


figure_row_1 = dbc.Row(
    [
        dbc.Col(
            [
                html.H4("Top Spending Sectors", className="mb-3"),
                html.Small("Select Range"),
                dcc.RangeSlider(
                    1,
                    15,
                    1,
                    value=[2, 10],
                    id="top_dector",
                    marks=None,
                    tooltip={"placement": "left", "always_visible": True},
                ),
                dcc.Graph(figure=graphs.get_pie(label, values)),
            ],
            md=5,
            style=stl.section,
        ),
        dbc.Col(
            [
                html.H4("Top Spending Products", className="mb-3"),
                html.Small("Select Range"),
                dcc.RangeSlider(
                    1,
                    15,
                    1,
                    value=[2, 10],
                    id="top_product",
                    marks=None,
                    tooltip={"placement": "left", "always_visible": True},
                ),
                dcc.Graph(figure=graphs.get_pie(label, values)),
            ],
            md=6,
            style=stl.section,
        ),
    ],
    align="center",
    justify="center",
)

figure_row_2 = dbc.Row(
    [
        dbc.Col(
            [
                html.H4(
                    "Top Spending Products for Selected Sector",
                    className="mb-3 font-bold",
                ),
                # html.Small("Select Sector"),
                dcc.Dropdown(
                    options=dlist.category,
                    placeholder="Select Sector",
                    className="mb-1",
                ),
                dcc.Graph(figure=graphs.get_bar(label, values)),
            ],
            md=5,
            style=stl.section,
        ),
        dbc.Col(
            [
                html.H4("Daily Spending Trend", className="mb-3"),
                dcc.Graph(figure=graphs.get_trend(label, values, values)),
            ],
            md=6,
            style=stl.section,
        ),
    ],
    align="left",
    justify="center",
)


figure_row_3 = dbc.Row(
    [
        dbc.Col(
            [   html.H4("Budget and Expense", className="mb-3"),
                dcc.Graph(figure=graphs.get_budget_bar(label, values, values))],
            md=6,
            style=stl.section,
        ),
        dbc.Col([
            html.H2("Bill Payment Status",className='text-center bg-info',style=stl.section),
            html.Br(),
            html.Br(),
            html.Div([html.H4("Home Rent ✅")],style={'textAlign':'left','marginLeft':'170px'}),
            html.Div([html.H4("Internet Bill ✅")],style={'textAlign':'left','marginLeft':'170px'}),
            html.Div([html.H4("Bua Bill ✅")],style={'textAlign':'left','marginLeft':'170px'}),
            html.Div([html.H4("Bike Parking Rent ❌")],style={'textAlign':'left','marginLeft':'170px'}),
            html.Div([html.H4("Electricity Bill ❌")],style={'textAlign':'left','marginLeft':'170px'}),

        ], md=5, style=stl.section),
    ],
    align="left",
    justify="center",
)


analysis_tab_current = [card_row, figure_row_1, figure_row_2, figure_row_3]
