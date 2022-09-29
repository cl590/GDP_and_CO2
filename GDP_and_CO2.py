import pandas as pd
file = pd.read_csv("https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv")
new_file = file[['Mortality rate, infant (per 1,000 live births)','GDP per capita (constant 2010 US$)', 'Country Name']]