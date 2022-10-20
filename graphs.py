import numpy as np
import plotly.express as px
import dash
from dash import dcc, html, dash_table, callback_context, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go

def get_tbl(data):
    tbl = dash_table.DataTable(
        data.to_dict("records"),
        [{"name": i, "id": i} for i in data.columns],
        style_data={"color": "black", "backgroundColor": "white", "textAlign": "left"},
        style_header={
            "backgroundColor": "#080808",
            "color": "white",
            "fontWeight": "bold",
            "textAlign": "left",
        },
        style_table={"overflowY": "scroll", "height": "150px"},
        style_data_conditional=[
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "#bbbfbf",
            }
        ],
    )
    return tbl

def get_small_tbl(data):
    tbl = dash_table.DataTable(
        data.to_dict("records"),
        [{"name": i, "id": i} for i in data.columns],
        style_data={"color": "black", "backgroundColor": "white", "textAlign": "left"},
        style_header={
            "backgroundColor": "#080808",
            "color": "white",
            "fontWeight": "bold",
            "textAlign": "left",
        },
        style_table={"overflowY": "scroll", "height": "80px",'width':'400px'},
        style_data_conditional=[
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "#bbbfbf",
            }
        ],
    )
    return tbl


def get_card(account,ammount,src):
    card = dbc.Card(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.CardImg(
                            src=src,
                            className="img-fluid rounded-start",
                        ),
                        className="col-md-4",
                    ),
                    dbc.Col(
                        dbc.CardBody(
                            [
                                html.H5(f"{account}", className="card-title"),
                                html.H6(f'{ammount}'+" "+"TK",
                                    className="card-text",
                                ),
                                # html.Small(
                                #     "Last updated 3 mins ago",
                                #     className="card-text text-muted",
                                # ),
                            ]
                        ),
                        className="col-md-8",
                    ),
                ],
                className="g-0 d-flex align-items-center",
            )
        ],
        style={"maxWidth": "200px"},outline=False
    )
    return card