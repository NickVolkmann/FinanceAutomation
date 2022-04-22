for i in range(len(cleaned_df)):
    row = cleaned_df['Soll/Haben'][i]
    if row == "H":
        new_row = {'Textschlüssel': cleaned_df['Textschlüssel'][i],
                   'Zahlungsempfänger': cleaned_df['Zahlungsempfänger'][i],
                   'Vorgang/Verwendungszweck': cleaned_df['Vorgang/Verwendungszweck'][i],
                   'Umsatz': cleaned_df['Umsatz'][i]}
        print(new_row)
        ser = pd.Series(data=new_row, index=['Textschlüssel'])
        df_haben = pd.concat([df_haben,ser], ignore_index=True)
        print(df_haben)
        print("ausgeführt")



        print("ausgeführt")
        s1_textschlüssel = pd.Series(["hallo"])
        s2_zahlungsempfänger = pd.Series(["asd"])
        s3_vorgang = pd.Series(["asd"])
        s4_umsatz = pd.Series(["asd"])
        df_haben = pd.concat([s1_textschlüssel, s2_zahlungsempfänger, s3_vorgang, s4_umsatz], ignore_index=True)
        print(df_haben)