
import dash
from dash import dcc, html, dash_table, callback_context, Input, Output, State, ctx
import dash_bootstrap_components as dbc
from datetime import date
import pandas as pd
import style as stl
from dash.exceptions import PreventUpdate
import dropdown_list as dlist
import tab_content as tc
import dataloader as dl
import graphs as gs


df = pd.read_csv("expense.csv")
df_income = pd.read_csv("income.csv")
df_budget = pd.read_csv("budget.csv")
final_inp = pd.DataFrame()
date_ = date.today()
final_inp_e = pd.DataFrame()
final_inp_b = pd.DataFrame()



app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1.0"}
    ],
)

header = dbc.Row(html.H1("Header", style=stl.header))









app.layout = dbc.Container(
    [
        header,
        dbc.Tabs(
            [
                dbc.Tab(
                    tc.input_tab,
                    label="Input Panel",
                    active_label_style={
                        "backgroundColor": "#ffe9fb",
                        "fontWeight": "bold",
                        "color": "black",
                    },
                ),
                dbc.Tab(html.Div(html.H3("Empty")), label="Analysis"),
            ],
        ),
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
    Input("add-b", "n_clicks"),
    Input("remove-b", "n_clicks"),
    Input("submit-b", "n_clicks"),
    Input("budget_cat", "value"),
    Input("budget_amm", "value"),
)
def write(
    add,
    remove,
    submit,
    cat,
    prod,
    price,
    add_2,
    remove_2,
    submit_2,
    acc,
    src,
    amm,
    add_3,
    remove_3,
    submit_3,
    bcat,
    bamm,
):
    global df
    global final_inp
    global df_income
    global final_inp_e
    global df_budget
    global final_inp_b

    if "add-i" == ctx.triggered_id:
        ins_data = pd.DataFrame(
            [[dl.date_, cat, prod, price]],
            columns=["entry_date", "category", "product", "cost"],
        )
        final_inp = pd.concat([final_inp, ins_data]).reset_index(drop=True)
        return [
            gs.get_tbl(final_inp),
            html.H6(
                "Record Added",
                className="text-center bg-primary text-light border-round mt-2 text-bold",
            ),
        ]

    elif "remove-i" == ctx.triggered_id:
        final_inp = final_inp[:-1]
        final_inp
        return [
            gs.get_tbl(final_inp),
            html.H6(
                "Record Removed",
                className="text-center bg-danger text-light border-round mt-2 text-bold",
            ),
        ]

    elif "submit-i" == ctx.triggered_id:
        df = pd.concat([df, final_inp]).reset_index(drop=True)
        df.to_csv("expense.csv", index=False)
        temp_df = final_inp
        final_inp = pd.DataFrame()
        return [
            gs.get_tbl(temp_df),
            html.H4(
                "Record Submitted",
                className="text-center bg-success text-light border-round mt-2 text-bold",
            ),
        ]

    elif "add-e" == ctx.triggered_id:
        ins_data_e = pd.DataFrame(
            [[dl.date_, acc, src, amm]],
            columns=["entry_date", "account", "source", "amount"],
        )
        final_inp_e = pd.concat([final_inp_e, ins_data_e]).reset_index(drop=True)
        return [
            gs.get_tbl(final_inp_e),
            html.H6(
                "Record Added",
                className="text-center bg-primary text-light border-round mt-2 text-bold",
            ),
        ]

    elif "remove-e" == ctx.triggered_id:
        final_inp_e = final_inp_e[:-1]
        final_inp_e
        return [
            gs.get_tbl(final_inp_e),
            html.H6(
                "Record Removed",
                className="text-center bg-danger text-light border-round mt-2 text-bold",
            ),
        ]

    elif "submit-e" == ctx.triggered_id:
        df_income = pd.concat([df_income, final_inp_e]).reset_index(drop=True)
        df_income.to_csv("income.csv", index=False)
        temp_df_e = final_inp_e
        final_inp_e = pd.DataFrame()
        return [
            gs.get_tbl(temp_df_e),
            html.H4(
                "Record Submitted",
                className="text-center bg-success text-light border-round mt-2 text-bold",
            ),
        ]

    elif "add-b" == ctx.triggered_id:
        ins_data_b = pd.DataFrame(
            [[bcat, bamm]],
            columns=["section", "amount"],
        )
        final_inp_e = pd.concat([final_inp_e, ins_data_b]).reset_index(drop=True)
        return [
            gs.get_tbl(final_inp_e),
            html.H6(
                "Record Added",
                className="text-center bg-primary text-light border-round mt-2 text-bold",
            ),
        ]
    elif "remove-e" == ctx.triggered_id:
        ins_data_b = ins_data_b[:-1]
        ins_data_b
        return [
            gs.get_tbl(ins_data_b),
            html.H6(
                "Record Removed",
                className="text-center bg-danger text-light border-round mt-2 text-bold",
            ),
        ]
    elif "submit-b" == ctx.triggered_id:
        df_budget = pd.concat([df_budget, final_inp_e]).reset_index(drop=True)
        df_budget.to_csv("budget.csv", index=False)
        temp_df_b = final_inp_e
        final_inp_b = pd.DataFrame()
        return [
            gs.get_tbl(temp_df_b),
            html.H4(
                "Record Submitted",
                className="text-center bg-success text-light border-round mt-2 text-bold",
            ),
        ]

    else:
        raise PreventUpdate


########## Original Expense Table Preveiw ################


@app.callback(
    Output("expense-tbl", "children"),
    Input("submit-i", "n_clicks"),
)
def main_df(a):
    return gs.get_tbl(df.sort_index(ascending=False))


############## Original Income Table Preview ################


@app.callback(
    Output("income-tbl", "children"),
    Input("submit-e", "n_clicks"),
)
def main_df(a):
    return gs.get_tbl(df_income.sort_index(ascending=False))


############## Original Income Table Preview ################
@app.callback(
    Output("budget-preview", "is_open"),
    [Input("see-budget-button", "n_clicks")],
    [State("budget-preview", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open




if __name__ == "__main__":
    app.run_server(debug=True, port=8000)
