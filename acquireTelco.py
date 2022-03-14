import os 
import env
import pandas as pd
from prepareTelco import clean_split_telco_data


# Function responsible for database connection. ()Sensivive data connection infomation protected for system integrity)
def db_connect(database, username = env.username, host = env.host, password = env.password):
        
    return f'mysql+pymysql://{env.username}:{env.password}@{env.host}/{database}'

# This function returns telco_churn data. First call checks whether the file exists in our local machine as csv file, 
# if not, it call the file from online resource through SQL query. 
def get_telco_data(use_cache = True):
    
    file_name = 'telco_churn.csv'
            
    if os.path.exists(file_name) and use_cache:
        
        print()
        
        print('\tProgram Status: Reading Raw Telco Data from a local cached csv file...')
        
        return pd.read_csv(file_name)
    
    database = 'telco_churn'
    
    url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/{database}'
    
    telco_sql_query = '''

            SELECT  c.churn, c.gender, c.tenure, c.partner, c.senior_citizen, 
            c.dependents, c.phone_service, c.multiple_lines, ist.internet_service_type,  
            ct.contract_type, cc.paperless_billing, c.tech_support, cp.monthly_charges, 
            cp.total_charges, pt.payment_type
            
                FROM customers c
                
                    JOIN internet_service_types ist  USING (internet_service_type_id)
                    JOIN contract_types ct USING (contract_type_id)
                    JOIN customer_contracts cc USING (customer_id)
                    JOIN customer_payments cp USING (payment_type_id)
                    JOIN payment_types pt USING (payment_type_id);

                    '''
    
    print()
    
    print('\tProgram Status: Acquiring data fresh from SQL Database...')
    
    print()
    
    telco_data = pd.read_sql(telco_sql_query, url)
    
    print('\n\tProgram Status: Saving data to local csv file...')
    
    print()
    
    telco_data.to_csv(file_name, index=False)
    
    
def clean_train_data(use_cache = True):
    
    cleaned_train = 'clean_train.csv'
                    
    if os.path.exists(cleaned_train) and use_cache:
        
        print()
        
        print('\tProgram Status: Reading cleaned train data from a local cached csv file...')
        
        return pd.read_csv(cleaned_train)
    
def clean_validate_data(use_cache = True):
    
    cleaned_validate = 'clean_validate.csv'
                    
    if os.path.exists(cleaned_validate) and use_cache:
        
        print()
        
        print('\tProgram Status: Reading cleaned validate data from a local cached csv file...')
        
        return pd.read_csv(cleaned_validate)
    
    
def clean_test_data(use_cache = True):
    
    cleaned_test = 'clean_test.csv'
                    
    if os.path.exists(cleaned_test) and use_cache:
        
        print()
        
        print('\tProgram Status: Reading cleaned test data from a local cached csv file...')
        
        return pd.read_csv(cleaned_test)
        

    
    
    
    

        
        

    
    
    
    
        
        