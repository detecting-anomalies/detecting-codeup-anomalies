import pandas as pd
import numpy as np

#------------------------------------------------------------

def Q_two(df, num=1):
    
    students = df.copy()
    #students = df.groupby(['cohort_id', 'endpoint']).agg('count')
    #students = students.sort_values(by= 'user_id', ascending= False)
    students = students.reset_index()
    students = students[students.endpoint != '/']
    
    count_df = students[['cohort_id', 'endpoint', 'count']]
    #count_df = count_df.rename(columns={'ip': 'count'})
    count_df.sort_values(by= ['cohort_id', 'count'], ascending= [False, False])
    
    new_df = count_df.sort_values(by= 'count', ascending= False).groupby('cohort_id').nth([0, num])
    
    return new_df

#------------------------------------------------------------

def student_df(df, program_id):
    
    students = df[df['program_id'] == program_id]
    
    students = students[students['endpoint'] != '/']
    
    students = students.groupby(['endpoint', 'cohort_id']).count()
    
    students = students.drop(columns=['id', 'name', 'slack', 'start_date', 'end_date', 
                                            'created_at', 'updated_at', 'program_id', 'user_id', 'student'])
    
    students = students.rename(columns={'ip': 'count'})
    
    students = students.reset_index()
    
    students = students.sort_values(by='count', ascending=False)
    
    return students

#------------------------------------------------------------

def web_scraping(df):
    
    df_2 = df.copy()
    
    df_2 = df_2[df_2['student'] == False]
    df_2 = df_2[df_2['endpoint'] != '/']
    
    df_2 = df_2.reset_index()
    
    df_3 = df_2.groupby(['date_time'])['endpoint'].agg(['count'])
    df_abnormal = df_3[df_3['count'] > 10]
    
    return df_2, df_abnormal

#------------------------------------------------------------



#------------------------------------------------------------

