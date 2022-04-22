import pandas as pd
import mysql.connector
from xlsxwriter import Workbook

mydb = mysql.connector.connect(host="localhost", user="root", password="fussball123")
cols = ['Buchungstag', 'Textschlüssel', 'Zahlungsempfänger','Vorgang/Verwendungszweck', 'Umsatz']
umsatz_januar = "C:/Users/nickv/OneDrive/Desktop/Finance_Automation/Umsatz_Maerz1.csv"

#definition of excel_writer
writer = pd.ExcelWriter('Overview.xlsx', engine="xlsxwriter")

df = pd.read_csv(umsatz_januar, delimiter=";", header=15, index_col=0, encoding="ISO-8859-1")
df_einkommen = pd.DataFrame(columns=cols)
df_ausgaben = pd.DataFrame(columns=cols)

cleaned_df = df[['Textschlüssel', 'Zahlungsempfänger','Vorgang/Verwendungszweck', 'Umsatz', 'Soll/Haben']].iloc[:len(df)-3]
cleaned_df = cleaned_df.sort_index()

for i in range(len(cleaned_df)):
    row = cleaned_df['Textschlüssel'][i]
    new_row = row.join(row.split(" ")[-1:])
    cleaned_df.at[cleaned_df.index[i], 'Textschlüssel'] = new_row

for i in range(len(cleaned_df)):
    row = cleaned_df['Soll/Haben'][i]
    if row == "H":
        df_append = (pd.DataFrame({'Buchungstag': [cleaned_df.index[i]],
                                   'Textschlüssel': [cleaned_df['Textschlüssel'][i]],
                                   'Zahlungsempfänger': [cleaned_df['Zahlungsempfänger'][i]],
                                   'Vorgang/Verwendungszweck': [cleaned_df['Vorgang/Verwendungszweck'][i]],
                                   'Umsatz': [cleaned_df['Umsatz'][i]]}))
        df_einkommen = pd.concat([df_einkommen,df_append], ignore_index=True)

    if row == "S":
        df_append = (pd.DataFrame({'Buchungstag': [cleaned_df.index[i]],
                                   'Textschlüssel': [cleaned_df['Textschlüssel'][i]],
                                   'Zahlungsempfänger': [cleaned_df['Zahlungsempfänger'][i]],
                                   'Vorgang/Verwendungszweck': [cleaned_df['Vorgang/Verwendungszweck'][i]],
                                   'Umsatz': [cleaned_df['Umsatz'][i]]}))
        df_ausgaben = pd.concat([df_ausgaben,df_append], ignore_index=True)

df_einkommen = df_einkommen.sort_values(by="Buchungstag")
df_ausgaben = df_ausgaben.sort_values(by="Buchungstag")

df.to_excel(writer, sheet_name="Overview")
df_einkommen.to_excel(writer, sheet_name="Einkommen")
df_ausgaben.to_excel(writer, sheet_name="Ausgaben")

writer.save()
print(df_einkommen)
print(df_ausgaben)