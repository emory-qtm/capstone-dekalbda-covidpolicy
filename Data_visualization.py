import pandas as pd
from matplotlib import pyplot
import numpy as np
import jenkspy

'''
How many cases are assigned a division to work on
'''
# Prosecutor = pd.read_csv('Data/Prosecutor Data-01-25-2023_name_rem.csv')
# Sentence = pd.read_csv('Data/Sentencing Information-01-25-2023_name_rem.csv')
#
# Daily_load = Prosecutor.CaseOriginDate.value_counts().rename_axis('Date').reset_index(name='Cases_Filed')
# Daily_load['Date']= pd.to_datetime(Daily_load['Date'])
# Daily_load = Daily_load.sort_values(by='Date')
# print(Daily_load)
# print(Daily_load.sort_values(by='Cases_Filed'))
# date = Daily_load["Date"]
# value = Daily_load["Cases_Filed"]
# pyplot.plot(date, value)
# pyplot.title('Time Series Count of Cases Load at Each Day from 2015 to 2019')
# pyplot.xlabel('Case Original Date')
# pyplot.ylabel('Cases Count')
# pyplot.show()

'''
How many felony and serious felony crime are committed and documented in the system per day
'''
# data = pd.read_csv('test.csv')
# data = data.drop(data[data.Degree.isin(['Misdemeanor', 'Ordinance', 'X', np.nan])].index)
# Daily_load = data.CaseOriginDate.value_counts().rename_axis('Date').reset_index(name='Cases_Filed')
# Daily_load['Date']= pd.to_datetime(Daily_load['Date'])
# Daily_load = Daily_load.sort_values(by='Date')
# print(Daily_load)
# date = Daily_load["Date"]
# value = Daily_load["Cases_Filed"]
# pyplot.plot(date, value)
# pyplot.title('Time Series Count of Number of Crime Committed at Each Day from 2015 to 2019 /n (Felony and Serious Felony only)')
# pyplot.xlabel('Case Original Date')
# pyplot.ylabel('Cases Count')
# pyplot.show()

'''
Bar graph of different cases
'''
#data = pd.read_csv('test.csv')
#data.fillna('Missing', inplace=True)
#Degree_count = data.Degree.value_counts().rename_axis('Degree').reset_index(name='Count')
#labels = Degree_count.Degree
#counts = Degree_count.Count

#fig, ax = pyplot.subplots(figsize=(16, 9))

#ax.barh(labels, counts)
#for s in ['top', 'bottom', 'left', 'right']:
#    ax.spines[s].set_visible(False)
#ax.xaxis.set_ticks_position('none')
#ax.yaxis.set_ticks_position('none')
#ax.xaxis.set_tick_params(pad=5)
#ax.yaxis.set_tick_params(pad=10)
#ax.grid(visibility=True, color='grey',
#        linestyle='-.', linewidth=0.5,
#        alpha=0.2)
#ax.invert_yaxis()

#for i in ax.patches:
#    pyplot.text(i.get_width() + 0.2, i.get_y() + 0.5,
#             str(round((i.get_width()), 2)),
#             fontsize=10, fontweight='bold',
#             color='grey')

#ax.set_title('Case counts by degree from 2015 to 2019',
#             loc='left', )
#pyplot.grid(visible=None)
#pyplot.show()

'''
case degree counts by month
'''
Prosecutor = pd.read_csv('Data/Prosecutor Data-01-25-2023_name_rem.csv')
Sentence = pd.read_csv('Data/Sentencing Information-01-25-2023_name_rem.csv')

Prosecutor['CaseOriginDate'] = pd.to_datetime(Prosecutor['CaseOriginDate'])
Prosecutor['month_year'] = Prosecutor['CaseOriginDate'].dt.to_period('M')
Prosecutor['month_year'] = Prosecutor['month_year'].astype("datetime64[ns]")
Daily_load = Prosecutor.month_year.value_counts().rename_axis('Date').reset_index(name='Cases_Filed')
Daily_load = Daily_load.sort_values(by='Date')
print(Daily_load)
date = Daily_load["Date"]
value = Daily_load["Cases_Filed"]
print(date)
print(value)
pyplot.plot(date, value)
pyplot.title('Time Series Count of Cases Load at Each Day from 2015 to 2019')
pyplot.xlabel('Case Original Date')
pyplot.ylabel('Cases Count')
pyplot.show()

y = np.array(value.tolist())
breaks = jenkspy.jenks_breaks(y, n_classes=6)
breaks_jkp = []
for v in breaks:
    idx = value.index[value == v]
    breaks_jkp.append(idx)
print(breaks_jkp)

'''
case per month per division
'''
data_div = data
data_div['JudgeandDivisionAssigned'] = data.JudgeandDivisionAssigned.str.extract('(\d+)') #get division number
data_div['CaseOriginDate'] = pd.to_datetime(data_div['CaseOriginDate'])
data_div['month_year'] = data_div['CaseOriginDate'].dt.to_period('M')
data_div['month_year'] = data_div['month_year'].astype(str)
data_div['month_year'] = pd.to_datetime(data_div['month_year'])
data_div = data_div.groupby(['JudgeandDivisionAssigned','month_year']).size().reset_index(name='counts')
data_div.set_index('month_year', inplace=True)
data_div.groupby('JudgeandDivisionAssigned')['counts'].plot(legend=True)
