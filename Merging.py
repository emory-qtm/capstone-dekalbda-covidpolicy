import pandas as pd
import numpy as np

Prosecutor_Data = pd.read_csv('Data/Prosecutor Data-01-25-2023.csv')
Sentencing_Data = pd.read_csv('Data/Sentencing Information-01-25-2023.csv')
Victim_Data = pd.read_csv('Data/Victim Data-01-25-2023.csv')

Sentencing_Data['Matching_ID'] = Sentencing_Data.CaseNbr + Sentencing_Data.PartyID.astype(str)
Prosecutor_Data['Matching_ID'] = Prosecutor_Data.CaseNumber + Prosecutor_Data.UniquePersonID.astype(str)

Merged = Sentencing_Data.merge(Prosecutor_Data, on='Matching_ID', how='left')
Merged.to_csv("test.csv")






