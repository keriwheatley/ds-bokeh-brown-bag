from bokeh.models import ColumnDataSource
import pandas as pd

# Load dataset as Pandas dataframe
def load_data():
    df = pd.read_csv('Issued_Construction_Permits.csv', low_memory=False)
    return df

# Preprocess dataset and return ColumnDataSource
def preprocess_data(df):
    
    data = df[(df['CalendarYearIssued'] >= 1980) &
          (df['PermitTypeDesc']=='Building Permit') &
          (df['StatusCurrent'].isin(['Final', 'Active', 'Closed']))
         ] \
    .groupby(['CalendarYearIssued'])['TotalJobValuation'].agg(['sum','mean','max','count']).reset_index().sort_values(by='CalendarYearIssued')

    data['TotalInBillions'] = data['sum']/1000000000
    data['AverageInBillions'] = data['mean']/1000000000
    data['MaxInBillions'] = data['max']/1000000000

    return ColumnDataSource(data)