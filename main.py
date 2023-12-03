# Import necessary library(s)
import functions as fn

# Define the location of the data sources
survey_file_loc_1 = "survey_ads.csv"
survey_file_loc_2 = "survey_organic.csv"
choices_file_loc = "questionnaire_choices.csv"

# Import csv files as dataframe
df_survey_1 = fn.csv_to_df(survey_file_loc_1)
df_survey_2 = fn.csv_to_df(survey_file_loc_2)
df_choices = fn.csv_to_df(choices_file_loc)

# Concatenate dataframes into single dataframe
df_survey_concat = fn.concat_df(df_survey_1, df_survey_2)

# Clean dataframes
df_survey_clean_1 = fn.remove_null(df_survey_concat)
df_survey_clean_2 = fn.remove_duplicate(df_survey_clean_1)

# Turn the dataframes into nested lists while removing unecessary columns
survey_unnecessary_col = ['timestamp']
survey_list = fn.df_to_list(df=df_survey_clean_2, col_to_rmv=survey_unnecessary_col)

choices_unnecessary_col = ['question','choice']
choices_list = fn.df_to_list(df=df_choices, col_to_rmv=choices_unnecessary_col)

# Define parameters of the conjoint analysis
valid_choices = ['A', 'B', 'C']
invalid_choice = 'D'
output_header = ["user_phone", "choice", "skill", "program_method", "program_price"]
output_file_loc = 'clean_data.csv'

# Run the data wrangling function
fn.conjoint_data_wrangling(survey_list=survey_list,
                           choices_list=choices_list,
                           valid_choices=valid_choices,
                           invalid_choice=invalid_choice,
                           output_header=output_header,
                           output_file_loc=output_file_loc)

# 