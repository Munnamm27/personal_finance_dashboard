import pandas as pd
from datetime import date


df = pd.read_csv("expense.csv")
df_income = pd.read_csv("income.csv")
df_budget = pd.read_csv("budget.csv")
final_inp = pd.DataFrame()
date_ = date.today()
final_inp_e = pd.DataFrame()
final_inp_b = pd.DataFrame()

