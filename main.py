import pandas as pd
import csv

umsatz_januar = "C:/Users/nickv/OneDrive/Desktop/Finance_Automation/Umsatz_Februar.csv"

df = pd.read_csv(umsatz_januar, delimiter=";", header=15, index_col=0, encoding="ISO-8859-1")
print(df.iloc[:len(df)-3])
