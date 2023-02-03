import pandas as pd

Prosecutor_Data = pd.read_csv('Data/Prosecutor Data-01-25-2023.csv')
Sentencing_Data = pd.read_csv('Data/Sentencing Information-01-25-2023.csv')
Victim_Data = pd.read_csv('Data/Victim Data-01-25-2023.csv')

Sentencing_Data['Matching_ID'] = Sentencing_Data.CaseNbr + Sentencing_Data.PartyID.astype(str)
Prosecutor_Data['Matching_ID'] = Prosecutor_Data.CaseNumber + Prosecutor_Data.UniquePersonID.astype(str)

Merged = Sentencing_Data.merge(Prosecutor_Data, on='Matching_ID', how='left')
Merged.to_csv("test.csv")

col_values = []
for col in Merged:
    col_values.append(Merged[col].unique())

col_names = []
for col in Merged.columns:
    col_names.append(col)

uniqe_value = {col_names[i]: col_values[i] for i in range(len(col_names))}

with open("unqie_value.txt", 'w') as f:
    for key, value in uniqe_value.items():
        f.write('%s:%s\n' % (key, value))






