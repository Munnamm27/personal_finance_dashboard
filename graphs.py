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




def get_pie(label,values):
    colors = px.colors.qualitative.D3

    fig = go.Figure(data=[go.Pie(labels=label,
                                values=values, hole=.35)])
    fig.update_traces(hoverinfo='label+value', textinfo='percent', textfont_size=14,
                    marker=dict(colors=colors, line=dict(color='#000000', width=1)))
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0),showlegend=True,legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))
    return fig

def get_bar(label,values):

    fig = go.Figure([go.Bar(x=values, y=label,orientation='h', text=values, marker=dict(
        color='green',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=1)
    ))])
    fig.update_layout(margin=dict(l=0, r=0, t=0, b=0), xaxis_title="Cost in TK",
    yaxis_title="Product Name",)
    return fig


def get_trend(day,spend,balance):
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=day, y=spend,
                        mode='lines+markers',
                        name='Spent Money'))
    fig.add_trace(go.Scatter(x=day, y=balance,
                        mode='lines+markers',
                        name='Available Balance'))
    fig.update_layout(margin=dict(l=0, r=45, t=30, b=0), xaxis_title="Date",
    yaxis_title="Cost in TK",legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="center",
    x=.5
))

    return fig

def get_budget_bar(product_name,budget,actual):

    fig = go.Figure([go.Bar(x=product_name, y=budget,orientation='v',name='Budget Amount', text=budget, marker=dict(
        color='green',
        line=dict(color='green', width=1)
    ))])
    fig.add_trace(go.Bar(x=product_name, y=actual,orientation='v',name='Spent Amount', text=actual, marker=dict(
        color='red',
        line=dict(color='red', width=1)
    )))
    fig.update_layout(margin=dict(l=0, r=40, t=40, b=0), xaxis_title="Cost in TK",barmode='group',
    yaxis_title="Product Name",legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="center",
    x=.5
))
    return fig