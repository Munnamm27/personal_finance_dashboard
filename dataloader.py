import pandas as pd
from datetime import date


df = pd.read_csv("expense.csv")
df_income = pd.read_csv("income.csv")
df_budget = pd.read_csv("budget.csv")
final_inp = pd.DataFrame()
date_ = date.today()
current_month = int(str(date_).split("-")[1])
previous_month = current_month - 1
final_inp_e = pd.DataFrame()
final_inp_b = pd.DataFrame()


category = [
    "Bike",
    "Bills",
    "Cloths",
    "Eating Out",
    "Entertainment",
    "Food",
    "Gifts",
    "Grocery",
    "Health",
    "Home Goods",
    "House",
    "Toiletry",
    "Transport",
    "To Her",
    "Others",
    "Unknown",
    "Untracked",
]

budget_list = [
    "Eating Out",
    "Electricity",
    "Entertainment",
    "To Her",
    "Mobile Recharge",
]

def date_spliter(data):
    data["month"] = data["entry_date"].apply(lambda x: int(x.split("-")[1]))
    data["date"] = data["entry_date"].apply(lambda x: int(x.split("-")[2]))
    data["year"] = data["entry_date"].apply(lambda x: int(x.split("-")[0]))


date_spliter(df)
date_spliter(df_income)


######Card Calculations#######
spent_amount=int(df[df['month']==current_month]['cost'].sum())
bank_1=int(df_income[df_income['account']=='SCB'].amount.sum())
bank_2=int(df_income[df_income['account']=='IBBL'].amount.sum())
cash_scb=int(df_income[(df_income['account']=='Cash Out') & (df_income['source']=='Salary')].amount.sum())
cash_ib=int(df_income[(df_income['account']=='Cash Out') & (df_income['source']=='Abbu')].amount.sum())
cash_gift=int(df_income[(df_income['account']=='Cash Out') & (df_income['source']=='Gift')].amount.sum())
total_cash=cash_scb+cash_ib+cash_gift-spent_amount
bank_scb=bank_1-cash_scb
bank_ib=bank_2-cash_ib
available=(total_cash+bank_scb+bank_ib)



# avalable_balance=int(df_income[df_income['month']==current_month])



def get_range_arrays_pie(d, col, start=1, end=10):
    data = (
        d.groupby(col).sum().sort_values("cost", ascending=False).iloc[start - 1 : end]
    )
    labels = data.index
    values = data["cost"].values
    return labels, values


def get_range_arrays_bar(d):
    data = d.groupby("product").sum()
    labels = data.index
    values = data["cost"].values
    return labels, values


def get_date_arrays(d):
    data = d.groupby("date").sum().sort_values("date")
    labels = data.index
    values = data["cost"].values
    return labels, values
