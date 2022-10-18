import numpy as np
import plotly.express as px
import dash
from dash import dcc, html, dash_table, callback_context, Input, Output, State, ctx
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from datetime import date
import pandas as pd
import style as stl
from dash.exceptions import PreventUpdate

df = pd.read_excel("expense.xlsx")
df_income=pd.read_excel('income.xlsx')
final_inp = pd.DataFrame()
date = date.today()
final_inp_e = pd.DataFrame()


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
        style_table={"overflowY": "scroll",'height':'280px'},
        style_data_conditional=[
            {
                "if": {"row_index": "odd"},
                "backgroundColor": "#bbbfbf",
            }
        ],
    )
    return tbl


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

header = dbc.Row(html.H1("Header", style=stl.header))


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
                dbc.Col([
                    html.H6("Expense Table",className='text-center'),
                    html.Div(id='expense-tbl'),
                        ], md=6),
                dbc.Col([
                    html.H6("Income Table",className='text-center'),
                    html.Div(id='income-tbl'),
                        ], md=6),
            ],
            style=stl.section
        ),
    ],
    width={"size": 8, "offset": 0, "order": 2},
)



input_tab= dbc.Row(
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

app.layout = dbc.Container(
    [
        header,
        dbc.Tabs( 
            [ 
                dbc.Tab(input_tab,label="Input Panel"),
                dbc.Tab(html.Div(html.H3("Empty")),label="Analysis"),
            ],    style={
                "backgroundColor": "#ffe9fb",
                    },
        )

    ],
    fluid=False,
    style={
        "backgroundColor": "#ffe9fb",
        "border": "3px black solid",
        "border-radius": "5px",
    },
)


# Expnese-Income Tab Callback ##


@app.callback(
    Output("input-tbl", "children"),
    # Output('expns-tbl',"children"),
    Input("add-i", "n_clicks"),
    Input("remove-i", "n_clicks"),
    Input("submit-i", "n_clicks"),
    Input("category", "value"),
    Input("product", "value"),
    Input("price", "value"),
    Input("add-e", "n_clicks"),
    Input("remove-e", "n_clicks"),
    Input("submit-e", "n_clicks"),
    Input("account", "value"),
    Input("source", "value"),
    Input("amount", "value"),
)
def write(add, remove, submit ,cat, prod,price,add_2,remove_2,submit_2,acc,src,amm):
    global df
    global final_inp
    global df_income
    global final_inp_e

    if "add-i" == ctx.triggered_id:
        ins_data = pd.DataFrame(
            [[date, cat, prod, price]], columns=["date", "category", "product", "cost"]
        )
        final_inp = pd.concat([final_inp, ins_data]).reset_index(drop=True)
        return [
            get_tbl(final_inp),
            html.H6(
                "Record Added",
                className="text-center bg-primary text-light border-round mt-2 text-bold",
            ),
        ]

    elif "remove-i" == ctx.triggered_id:
        final_inp = final_inp[:-1]
        final_inp
        return [
            get_tbl(final_inp),
            html.H6(
                "Record Removed",
                className="text-center bg-danger text-light border-round mt-2 text-bold",
            ),
        ]

    elif "submit-i" == ctx.triggered_id:
        df = pd.concat([df, final_inp]).reset_index(drop=True)
        df.to_excel("expense.xlsx", index=False)
        temp_df=final_inp
        final_inp = pd.DataFrame()
        return [
            get_tbl(temp_df),
            html.H4(
                "Record Submitted",
                className="text-center bg-success text-light border-round mt-2 text-bold",
            ),
        ]

    elif "add-e" == ctx.triggered_id:
        ins_data_e = pd.DataFrame(
            [[date, acc, src, amm]], columns=["date", "account", "source", "amount"]
        )
        final_inp_e = pd.concat([final_inp_e, ins_data_e]).reset_index(drop=True)
        return [
            get_tbl(final_inp_e),
            html.H6(
                "Record Added",
                className="text-center bg-primary text-light border-round mt-2 text-bold",
            ),
        ]

    elif "remove-e" == ctx.triggered_id:
        final_inp_e = final_inp_e[:-1]
        final_inp_e
        return [
            get_tbl(final_inp_e),
            html.H6(
                "Record Removed",
                className="text-center bg-danger text-light border-round mt-2 text-bold",
            ),
        ]

    elif "submit-e" == ctx.triggered_id:
        df_income = pd.concat([df_income, final_inp_e]).reset_index(drop=True)
        df_income.to_excel("income.xlsx", index=False)
        temp_df_e=final_inp_e
        final_inp_e = pd.DataFrame()
        return [
            get_tbl(temp_df_e),
            html.H4(
                "Record Submitted",
                className="text-center bg-success text-light border-round mt-2 text-bold",
            ),
        ]
    else:
        raise PreventUpdate



########## Original Expense Table Preveiw ################

@app.callback(
    Output('expense-tbl',"children"),
    Input("submit-i", "n_clicks"),
)
def main_df(a):
    return get_tbl(df.sort_index(ascending=False))

############## Original Income Table Preview ################

@app.callback(
    Output('income-tbl',"children"),
    Input("submit-e", "n_clicks"),
)
def main_df(a):
    return get_tbl(df_income.sort_index(ascending=False))

if __name__ == "__main__":
    app.run_server(debug=True, port=8000)
