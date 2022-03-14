import pandas as pd
from random import random
import math
from numpy import nan

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

def clean_telco(df):
    '''
    This function takes in dataframe as argument, 
    create dummy variables out of sex and embarked, and concats those to original dataframe
    drops columns embarked, sex, deck, class
    drops rows where age (177 rows) or embarked_town (2 rows) are null. 
    it returns the new cleaned dataframe.
    '''
    
    # Strip whitespaces from total and monthly charges

#     df['monthly_charges'] = df.monthly_charges.apply(str).str.replace('', '')
#     df['total_charges'] = df.total_charges.apply(str).str.replace('', '')

#     df['total_charges'] = df['total_charges'].strip()    
#     df['monthly_charges'] = df['monthly_charges'].strip()

    
    # Convert monthly and total charges to float
    df['monthly_charges'] = df.monthly_charges.astype(float)
    
    # Force the total charges data type from object to float
    df['total_charges'] = pd.to_numeric(df['total_charges'], errors = 'coerce')

     # Encode binary categorical variables to numeric
    df['enc_churn'] = df.churn.map({'Yes': 1, 'No': 0})
#     df['enc_gender'] = df.gender.map({'Female': 1, 'Male': 0})
#     df['enc_senior_citizen'] = df.senior_citizen.map({'Yes': 1, 'No': 0})
    df['enc_partner'] = df.partner.map({'Yes': 1, 'No': 0})
    df['enc_dependents'] = df.dependents.map({'Yes': 1, 'No': 0})
    df['enc_phone_service'] = df.phone_service.map({'Yes': 1, 'No': 0})
    df['enc_paperless_billing'] = df.paperless_billing.map({'Yes': 1, 'No': 0})
#     df['enc_multiple_lines'] = df.multiple_lines.map({'Yes': 1, 'No': 0, 'NaN':9})
#     df['enc_tech_support'] = df.tech_support.map({'Yes': 1, 'No': 0, 'NaN':9})
    df['enc_payment'] = df.payment_type.map({'Electronic check': 1, 'Mailed check': 2, 
                                             'Bank transfer (automatic)': 3, 'Credit card (automatic)': 4})
    
    df['enc_contract_type'] = df.contract_type.map({'Month-to-month': 1, 'One year': 2, 'Two year': 3})
    df['enc_intenet_service_type'] = df.internet_service_type.map({'DSL': 1, 'Fiber optic': 2, 'None': 3})

#      # Get dummies data for non-binary categorical data
#     dummies_df = pd.get_dummies(df[['payment_type','internet_service_type', 'contract_type']], drop_first=True)

#     df_with_dummies = pd.concat([df, dummies_df], axis=1)
    
#     df_with_dummies = df_with_dummies.drop_duplicates()

    df = df.drop_duplicates()
     
    df = df.drop(columns=['gender', 'partner', 'dependents','senior_citizen', 'phone_service',
#                          'multiple_lines', 'tech_support'
                          'contract_type','paperless_billing','payment_type',
                          'internet_service_type'])
    
#     df_dropped_cols_with_dummies = df_with_dummies.drop(columns=['gender', 'partner', 
#                                                                  'dependents','senior_citizen', 'phone_service',
#                                                                  'multiple_lines', 'contract_type',
#                                                                  'paperless_billing','payment_type','internet_service_type',
#                                                                  'tech_support'])
    
    df_cleaned = df[df.churn.notnull()]
    
    return df_cleaned

def train_validate_test_split(prepped_df, seed=123):
    '''
    This function takes in a cleaned dataframe and a random seed, 
    and splits the dataframe into 3 samples, a train, validate and test sample, 
    The test is 20% of the data, the validate is 24% of the data, and the train is 56% of the data. 
    The function returns 3 dataframes in the order of: train, validate and test. 
    '''
    train_and_validate, test = train_test_split(
                                                prepped_df, test_size=0.2, 
                                                random_state=seed, 
                                                stratify=prepped_df.churn
                                                )
    
    train, validate = train_test_split(
                                        train_and_validate,
                                        test_size=0.3,
                                        random_state=seed,
                                        stratify=train_and_validate.churn,
                                    )
    return train, validate, test


def clean_split_telco_data(df, target = 'churn', seed = 123):
    '''
    this function runs both the clean_telco and train_validate_test_split functions, initially taking in the orginal
    acquired dataframe as an argument and returning the 3 samples in order: train, validate, test. 
    '''
    cleaned_df = clean_telco(df)
    
    train, validate, test = train_validate_test_split(cleaned_df, seed=123)
    
    train = train.drop_duplicates()
    validate = validate.drop_duplicates()
    test = test.drop_duplicates()

    col_to_drop = ['customer_id']

    train = train.drop(columns = col_to_drop, errors = 'ignore')
    validate = validate.drop(columns = col_to_drop, errors='ignore')
    test = test.drop(columns = col_to_drop, errors='ignore')

    train = train.reset_index(drop = True)
    validate = validate.reset_index(drop = True)
    test = test.reset_index(drop = True)

    rename_cols = {'payment_type_Credit card (automatic)':'credit_card_pay',
                    'payment_type_Electronic check':'electronic_pay',
                    'payment_type_Mailed check':'mailed_check_pay',
                    'internet_service_type_Fiber optic':'fiber_optic_internet_service',
                    'nternet_service_type_None':'no_internet_subscription',
                    'contract_type_One year':'one_year_contract',
                    'contract_type_Two year':'two_year_contract'}

    train = train.rename(columns = (rename_cols))
    validate = validate.rename(columns = (rename_cols))
    test = test.rename(columns = (rename_cols))
    
    # Save new cleaned csv files to local directory for ease of exploration analysis
    clean_train = 'clean_train.csv'
    clean_validate = 'clean_validate.csv'
    clean_test = 'clean_test.csv'
    
    train.to_csv(clean_train, index = False)
    validate.to_csv(clean_validate, index = False)
    test.to_csv(clean_test, index = False)

    return train, validate, test








