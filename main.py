import pandas as pd
import numpy as np

def csv_to_df(file_loc):
    df = pd.read_csv(file_loc)
    
    return df


def remove_null(df):
    df_clean = df.dropna()
    
    return df_clean


def remove_duplicate(df):
    df_clean = df.drop_duplicates()
    
    return df_clean