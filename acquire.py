import pandas as pd
import numpy as npo
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



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------



#------------------------------------------------------------