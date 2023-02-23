# essential imports
import pandas as pd
import numpy as np
import os

# .py file
import env

#nuissance import
import warnings
warnings.filterwarnings("ignore")
#-------------acquire---------------------

# setting connectiong to sequel server using env
def get_connection(db, user=env.username, host=env.host, password=env.password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'



##################
 
# acquiring telco data using a different function

def get_logs_data(get_connection):
    filename = "logs_team.csv"
    
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col = 0)
    
    else:
        
    # read the SQL query into a dataframe
        df = pd.read_sql(
    
        '''
           select user_id as id, cohort_id as cohort,ip,path as endpoint, `time`,`date`,program_id,updated_at,deleted_at,created_at,end_date,start_date,
            `name` 

            from cohorts
            right join `logs`
            on cohorts.id = `logs`.user_id
    
        
        ''', get_connection('curriculum_logs'))

    # Write that dataframe to disk for later. Called "caching" the data for later.
        df.to_csv(filename)

    # Return the dataframe to the calling code
    return df 


#-------------prepare--------------------

def prepare(df):
    
    '''
    Input: Dataframe
    Output: Cleaned Dateframe, dataframe of students, groupby/agg dataframe, and dataframe which holds student id 62
    '''
    
    df['datetime'] = df.date +" "+ df.time
    
    #create datetime
    df.datetime = pd.to_datetime(df.datetime)
    
    #sort index
    df = df.set_index(df.datetime).sort_index()
    
    # drop columns 
    df = df.drop(columns= ['time','date','deleted_at'])
    
    # finding all verifiable students
    students = df[df.start_date.notnull()]
    
    # create a groupby dataframe to show activity
    page_views_per_student = students.groupby(['id'])['endpoint'].agg(['count'])
    
    # change column name
    page_views_per_student = page_views_per_student.rename(columns={'count':'pages_accessed'}) 
    
    # a quick dataframe peak at a student with low activty
    student62 = students[students.id == 62]
    
    return df,students, page_views_per_student ,student62

def grad_activity(df):
    
    '''
    Input: Dataframe
    Output:
    '''
    
    # creating datetime
    df.start_date = pd.to_datetime(df.start_date)
    df.end_date = pd.to_datetime(df.end_date)
    
    # creating a feature of time in class before graduating or ending.
    df['time_in_class'] = df.end_date - df.start_date 
    
    # removing students who make not have been entirely enrolled
    df = df[df.name != 'Placeholder for students in transition']
    
    # removing staff members
    df = df[df.name != 'Staff']
    
    # finding access points where someone made a query after their graduation or end date
    df_aftergrad = df[df.datetime > df.end_date]
    
    # separating df by programs
    df_aftergrad1 = df_aftergrad[df_aftergrad.program_id == 1.0]
    df_aftergrad2 = df_aftergrad[df_aftergrad.program_id == 2.0]
    df_aftergrad4 = df_aftergrad[df_aftergrad.program_id == 4.0]
    
    # program 1
    df_aftergrad1 = df_aftergrad1.groupby("endpoint")['datetime'].agg(['count'])
    
    # program is looking at these 
    program1_tops = df_aftergrad1.sort_values(by = 'count').tail(3)
    
    
    # program 2
    df_aftergrad2 = df_aftergrad2.groupby("endpoint")['datetime'].agg(['count'])
    
    # program is looking at these 
    program2_tops = df_aftergrad2.sort_values(by = 'count').tail(3)
    
    
    # program 4
    df_aftergrad4 = df_aftergrad4.groupby("endpoint")['datetime'].agg(['count'])
    
    # program is looking at these 
    program4_tops = df_aftergrad4.sort_values(by = 'count').tail(3)
    
    
    return program1_tops, program2_tops, program4_tops


    
    
    
    
    


