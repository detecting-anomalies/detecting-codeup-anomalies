import pandas as pd
import numpy as np
import os
from env import host, username, password

#------------------------------------------------------------

def get_connection(db, user=username, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'
    
#------------------------------------------------------------

def get_codeup_data():

    if os.path.isfile('codeup_data.csv'):
        
        df = pd.read_csv('codeup_data.csv')
        df = df.drop(columns='Unnamed: 0')

        return df
    
    else:
        
        url = get_connection('curriculum_logs')
        query = '''
                SELECT *
                FROM cohorts
                RIGHT JOIN `logs` ON(cohorts.id=logs.user_id); 
                '''
        df = pd.read_sql(query, url)                
        df.to_csv('codeup_data.csv')

        return df

#------------------------------------------------------------

def wrangle_codeup():
    
    df = get_codeup_data()
    
    df['date_time'] = df['date'] + ' ' + df['time']
    df = df.drop(columns=['date', 'time'])
    
    df['date_time'] = pd.to_datetime(df['date_time'])
    df['start_date'] = pd.to_datetime(df['start_date'])
    df['end_date'] = pd.to_datetime(df['end_date'])
    df['created_at'] = pd.to_datetime(df['created_at'])
    df['updated_at'] = pd.to_datetime(df['updated_at'])
    df['deleted_at'] = pd.to_datetime(df['deleted_at'])
    df['student'] =  df['start_date'].notnull()
    
    df = df.set_index('date_time')
    df = df.drop(columns='deleted_at')
    
    df = df.rename(columns={'path': 'endpoint'})
    df = df.sort_index()
        
    return df

#------------------------------------------------------------

def check_staff(df):
    
    staff = df[df['name'] == 'Staff']
    
    num_staff = staff['user_id'].nunique()
    
    staves = pd.DataFrame(staff['endpoint'].unique())
    
    print(f'There is {num_staff} staff member(s)')
    
    return staves

#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------