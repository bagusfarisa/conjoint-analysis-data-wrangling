# Import necessary library(s)
import pandas as pd


# Define function to import csv as dataframe
def csv_to_df(file_loc):
    df = pd.read_csv(file_loc)
    
    return df


# Define function to concatenate dataframes
def concat_df(*dfs):
    df_list = []
    
    for i in dfs:
        df_list.append(i)    
    
    df_concat = pd.concat(df_list, axis=0)
    
    return df_concat

# Define function to remove row with missing value(s)
def remove_null(df):
    df_clean = df.dropna()
    
    return df_clean


# Define function to remove duplicates in a dataframe
def remove_duplicate(df):
    df_clean = df.drop_duplicates()
    
    return df_clean


# Define function to convert dataframe into nested list
def df_to_list(df, col_to_rmv=[]):
    df_clean = df.drop(col_to_rmv, axis=1)
    list = df_clean.values.tolist()
    
    return list


# Define function to convert lists into clean data format
def conjoint_data_wrangling(survey_list, choices_list, valid_choices, invalid_choice, output_header, output_file_loc):
    
    # Create an empty Conjoint List
    conjoint_list = []

    # Fill in the list by iterating the 
    for i in survey_list:
        
        for j in range(len(i)-1):
            j = j+1
            
            n_of_choices = len(valid_choices)
            for choice in valid_choices:
                list = []
                user_choice = i[j].split(",")
                list.append(i[0])
                if invalid_choice in user_choice:
                    list.append(0)
                elif choice in user_choice:
                    list.append(1)
                else:
                    list.append(0)
                
                row_number = 3 * j - n_of_choices
                for item in choices_list[row_number]:
                    list.append(item)
                
                n_of_choices = n_of_choices - 1
                conjoint_list.append(list)
            
    header = output_header
    conjoint_list.insert(0, header)

    df_clean_data = pd.DataFrame(conjoint_list[1:], columns=conjoint_list[0])
    df_clean_data.to_csv(output_file_loc, index=False)
    
    print('Data wrangling process finished. \nYou file is exported as', output_file_loc)