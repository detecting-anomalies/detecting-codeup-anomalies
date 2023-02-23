#Imports
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


#compute bollinger bands
def compute_bollinger(series, column, span, k):

    mean_df = series.ewm(span=span).mean()
    std_df = series.ewm(span=span).std()
    upper_band = mean_df + std_df * k
    lower_band = mean_df - std_df * k
    final_df = pd.concat([series, mean_df, upper_band, lower_band], axis= 1)
    final_df.columns = [column, 'midband', 'ub', 'lb']
    final_df['pct_b'] = (final_df[column] - final_df['lb']) / (final_df['ub'] - final_df['lb'])

    return final_df



#plot exponential moving average
def plot_ema(df, title):
    plt.figure(figsize=(13, 7))
    plt.plot(df, label='Original')
    plt.xlabel('Date')
    plt.ylabel('Number of hits')
    plt.title(f'{title}EMA of website hits over time')
    plt.legend()
    plt.show()


# 2 new dfs, Data Science and Web Dev
def seperate_programs(df):
    '''
    makes 2 new dfs from original df, 1 for data science 
    students and the other for web dev students
    '''
    #program_id 3 is Data Science, this pulls all rows with 3 for program_id
    datsci_df = df.loc[df['program_id'] == 3]
   
    webdev_df1 = df.loc[df['program_id'] == 1 ]
    webdev_df2 = df.loc[df['program_id'] == 2 ]
    webdev_df4 = df.loc[df['program_id'] == 4 ]

    webdev_df = pd.concat([webdev_df1, webdev_df2, webdev_df4])

    return datsci_df, webdev_df


'''
def get_boll_w_m_q(column):
    weekly_avg = daily_hits.ewm(span=7).mean()
    monthly_avg = daily_hits.ewm(span=30).mean()
    quarterly_avg = daily_hits.ewm(span=90).mean()

    weekly_boll = compute_bollinger(weekly_avg, column, span= 7, k=1.5)
    monthly_boll = compute_bollinger(monthly_avg, column, span= 30, k=1.5)
    quarterly_boll = compute_bollinger(quarterly_avg, column, span= 90, k=1.5)
'''

def resample_to_plot_pipeline(df, col_to_resamp, W_M_Q, span, k=1.5):
    '''
    in progress
    '''
    daily_hits = df[col_to_resamp].resample(W_M_Q).count()
    daily_hits.sort_values(ascending= False)
    weekly_avg = daily_hits.ewm(span=span).mean()
    weekly_boll = compute_bollinger(weekly_avg, 'hits', span= span, k=k)

    return 


def wrangle_resample_plot_cohort (df, time):
    '''
    this takes in either datsci_df or webdev_df and drops columns
    '''
    df['date'] = pd.to_datetime(df['date'], infer_datetime_format=True)
    df = df.set_index('date')
    df = df.drop(columns= ['name', 'slack', 'deleted_at'])
    df = df['path'].resample(time).count()
    df.plot()
    return df

